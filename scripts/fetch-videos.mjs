#!/usr/bin/env node
/**
 * Fetch Tom's YouTube videos and rank them by view count.
 *
 * Runs before `astro build`. YouTube's public RSS feed
 * (feeds/videos.xml?channel_id=...) needs no API key and returns the
 * 15 most recent uploads WITH view counts and publish dates.
 *
 * Shorts: the RSS feed DOES include them. Shorts are excluded from the
 * ranking by probing each thumbnail — a Short has no 16:9 maxresdefault.jpg
 * (YouTube serves it at most 1:1 or not at all), whereas a normal video
 * always has a 1280x720 maxres. That is done offline below via
 * `detectShorts` so the probe happens once, not on every build.
 *
 * Output: src/data/videos.json
 */

import { writeFileSync, mkdirSync, readFileSync, existsSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const OUT = resolve(__dirname, '../src/data/videos.json');

const CHANNEL_ID = process.env.YOUTUBE_CHANNEL_ID || 'UCqy-iXx82rhNv9QFqLnVvzQ';

// How many videos to keep in videos.json (the site shows the first 4).
const KEEP = 12;

async function hasLandscapeThumb(id) {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), 8000);
    try {
        const res = await fetch(`https://i.ytimg.com/vi/${id}/maxresdefault.jpg`, {
            signal: controller.signal,
            method: 'HEAD',
            headers: { 'User-Agent': 'portfolio-build/1.0' }
        });
        return res.ok;
    } catch {
        // Network hiccup: do not silently drop the video.
        return true;
    } finally {
        clearTimeout(timer);
    }
}

/** Resolve which of the candidates are Shorts, in parallel. */
async function detectShorts(candidates) {
    const flags = await Promise.all(candidates.map((v) => hasLandscapeThumb(v.id)));
    const shorts = new Set();
    candidates.forEach((v, i) => {
        if (!flags[i]) shorts.add(v.id);
    });
    return shorts;
}

/** Best signal: the feed entry itself links to /shorts/ID for Shorts. */
function feedShorts(candidates) {
    const shorts = new Set();
    for (const v of candidates) {
        if (v.isShort) shorts.add(v.id);
    }
    return shorts;
}

/** Duration like "15:42" via yt-dlp (present on the build machine). */
function fetchDuration(id) {
    try {
        const out = execFileSync(
            'yt-dlp',
            ['--no-playlist', '--skip-download', '--print', '%(duration_string)s', `https://www.youtube.com/watch?v=${id}`],
            { timeout: 30000, encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] }
        );
        const d = out.trim().split('\n').pop() || '';
        // YouTube badges always show m:ss — plain seconds come back as "30".
        return /^\d+$/.test(d) ? `0:${String(d).padStart(2, '0')}` : d || undefined;
    } catch {
        return undefined;
    }
}

// Videos to exclude from ranking entirely (unlisted, mistakes, etc).
const EXCLUDE_IDS = new Set([]);

function decode(s) {
    return s
        .replace(/&amp;/g, '&')
        .replace(/&lt;/g, '<')
        .replace(/&gt;/g, '>')
        .replace(/&quot;/g, '"')
        .replace(/&#39;/g, "'")
        .replace(/&apos;/g, "'");
}

function parseFeed(xml) {
    const entries = xml.split('<entry>').slice(1);
    return entries.map((entry) => {
        const pick = (tag) => {
            const m = entry.match(new RegExp(`<${tag}[^>]*>([\\s\\S]*?)</${tag}>`));
            return m ? decode(m[1].trim()) : '';
        };
        const id = (entry.match(/<yt:videoId>([\w-]+)<\/yt:videoId>/) || [])[1] || '';
        const views = (entry.match(/views="(\d+)"/) || [])[1];
        const thumbnail = (entry.match(/<media:thumbnail url="([^"]+)"/) || [])[1] || '';
        return {
            id,
            title: pick('title'),
            published: pick('published'),
            views: views ? Number(views) : null,
            thumbnail,
            isShort: /\/shorts\//.test(entry)
        };
    });
}

async function fetchFeed() {
    const url = `https://www.youtube.com/feeds/videos.xml?channel_id=${CHANNEL_ID}`;
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), 15000);
    try {
        const res = await fetch(url, {
            signal: controller.signal,
            headers: { 'User-Agent': 'portfolio-build/1.0' }
        });
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return await res.text();
    } finally {
        clearTimeout(timer);
    }
}

async function main() {
    let videos = [];

    try {
        const xml = await fetchFeed();
        videos = parseFeed(xml);
        console.log(`[videos] RSS returned ${videos.length} entries`);
    } catch (err) {
        console.warn(`[videos] RSS fetch failed (${err.message}) — using cached snapshot`);
    }

    const candidates = videos.filter((v) => v.id && !EXCLUDE_IDS.has(v.id));

    // Shorts are excluded via two signals: the feed entry URL (/shorts/ID)
    // and the thumbnail probe (a Short has no landscape maxres asset).
    const shortIds = feedShorts(candidates);
    for (const id of await detectShorts(candidates)) shortIds.add(id);
    if (shortIds.size) {
        console.log(`[videos] skipping ${shortIds.size} Short(s): ${[...shortIds].join(', ')}`);
    }

    // Manual fields (duration, channelName, …) must survive future builds.
    let previous = new Map();
    if (existsSync(OUT)) {
        try {
            for (const v of JSON.parse(readFileSync(OUT, 'utf8'))) previous.set(v.id, v);
        } catch {
            /* unreadable cache: start fresh */
        }
    }

    videos = candidates
        .filter((v) => !shortIds.has(v.id))
        .sort((a, b) => (b.views ?? 0) - (a.views ?? 0))
        .slice(0, KEEP)
        .map((v, i) => {
            const prev = previous.get(v.id) || {};
            return {
                rank: i + 1,
                id: v.id,
                title: v.title,
                views: v.views,
                published: v.published.slice(0, 10),
                watchUrl: `https://www.youtube.com/watch?v=${v.id}`,
                embedId: v.id,
                channelName: prev.channelName || 'Tom Szenessy',
                thumbnailUrl: `https://i.ytimg.com/vi/${v.id}/maxresdefault.jpg`,
                ...(prev.duration ? { duration: prev.duration } : {})
            };
        });

    // Fill missing durations once (yt-dlp); the merge above keeps them forever.
    for (const v of videos) {
        if (!v.duration) {
            const d = fetchDuration(v.id);
            if (d) {
                v.duration = d;
                console.log(`[videos] duration ${v.id}: ${d}`);
            } else {
                console.warn(`[videos] duration missing for ${v.id} — fill videos.json manually`);
            }
        }
    }

    if (!videos.length) {
        console.warn('[videos] no videos resolved — leaving existing videos.json untouched');
        return;
    }

    mkdirSync(dirname(OUT), { recursive: true });
    writeFileSync(OUT, JSON.stringify(videos, null, 2) + '\n');
    console.log(`[videos] wrote ${videos.length} to src/data/videos.json`);
    for (const v of videos) {
        console.log(`  #${v.rank} ${String(v.views).padStart(6)}  ${v.title.slice(0, 55)}`);
    }
}

main();
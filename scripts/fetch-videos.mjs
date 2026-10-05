#!/usr/bin/env node
/**
 * Fetch Tom's YouTube videos and rank them by view count.
 *
 * Runs before `astro build`. YouTube's public RSS feed
 * (feeds/videos.xml?channel_id=...) needs no API key and returns the
 * 15 most recent uploads WITH view counts and publish dates.
 *
 * NOTE: the RSS feed does NOT include Shorts. If Shorts should rank,
 * they must be added manually below (see PINNED / EXTRA_SHORT_IDS).
 *
 * Output: src/data/videos.json
 */

import { writeFileSync, mkdirSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const OUT = resolve(__dirname, '../src/data/videos.json');

const CHANNEL_ID = process.env.YOUTUBE_CHANNEL_ID || 'UCqy-iXx82rhNv9QFqLnVvzQ';

// How many videos to keep in videos.json (the site shows the first 4).
const KEEP = 12;

// Shorts never appear in the RSS feed. Add IDs here if they should count.
const EXTRA_SHORT_IDS = [];

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
            thumbnail
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

    // Merge manually-listed Shorts (not in RSS).
    if (EXTRA_SHORT_IDS.length) {
        console.log(`[videos] adding ${EXTRA_SHORT_IDS.length} manual Short IDs`);
    }

    videos = videos
        .filter((v) => v.id && !EXCLUDE_IDS.has(v.id))
        .sort((a, b) => (b.views ?? 0) - (a.views ?? 0))
        .slice(0, KEEP)
        .map((v, i) => ({
            rank: i + 1,
            id: v.id,
            title: v.title,
            views: v.views,
            published: v.published.slice(0, 10),
            watchUrl: `https://www.youtube.com/watch?v=${v.id}`,
            embedId: v.id
        }));

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
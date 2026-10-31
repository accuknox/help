Subject: Guard 1.1 blogs, I gave both a proper rework

Hi Nat, Rahul, Syed and Debjani,

Thanks for getting both Guard 1.1 posts out so fast while I was away. I went back into the leaderboard data this week and found a better story than the one we told, so I reworked both posts around it.

Here it is in one line. Guard 1.1 doesn't win any of the 19 groups. It's #1 because its worst group (0.536) is better than anyone else's worst group. For a CISO, that's the number that matters, because attackers go after your weakest spot.

Both posts are in one Google Doc, one tab each. Anyone at AccuKnox can edit it: [Guard 1.1 blogs, business and technical](DOC_URL)

**Nat, your business post**

- It had no images in the body. Now it has 6, including 2 short GIFs and a screenshot of the live ranking. I also made a new cover from the real scores, so the cover itself is proof.
- Every number now links to its source: the leaderboard, its scoring method, or the public thread where HiveTrace confirms they ran the test themselves.
- I added a small table a CISO can use today. It maps 5 kinds of AI app to the leaderboard group worth checking.
- Two new numbers do the selling for us. We block about 814 fewer real users per 10,000 safe prompts than the runner-up. On safe security-training prompts, we block 25 in 100 and Qwen3Guard blocks 79.
- I fixed a few things readers would trip on. The link to Rahul's post returned an error, one heading ran into the next line, and I cut the quotes from 6 to 2.
- Our writing checker flagged 22 critical issues before. It flags none now.

**Rahul, your technical post**

- It went from 2 images to 9: a heatmap of every group, 4 charts, 2 leaderboard screenshots and 2 GIFs.
- There's a new per-group table with our rank out of 41. It also shows the finding I'd lead with in any talk: if the runner-up fixed just its one weak group, it would score 0.823 and take first place.
- The old diagram showed a separate decision layer, and the model card describes something different. The new diagram matches the card: one model that returns a probability. The code snippet from the card is in there as well.
- We now say plainly where we're behind. Prompt injection is 0.706, rank 21 of 41. I kept our own 0.964 result but labeled it as ours. Engineers trust a post more when it admits a gap.
- The post links the raw CSV and JSON files, so any engineer can check every number for themselves.
- Our writing checker flagged 12 critical issues before. It flags none now. Both posts also got FAQs, a video and a filled SEO table.

**Two things I need from you before we publish**

1. Our sales email says we're "well ahead" on prompt injection and "#1 of 41 vendors". The board ranks 41 models, not vendors, and the runner-up beats us on prompt injection. Can we fix the template before more emails go out? I'm happy to draft it.
2. Could you look at the new business cover and tell me if it works? And is the model available on-prem yet? I left that out of both posts until we're sure.

Happy to walk anyone through it on a quick call.

Thanks,
Atharva

# AccuKnox Best Practices Cheat Sheets Launch

Ten gated cheat sheets, one per AccuKnox module, are ready to launch. Open your own folder and start with step 1 of your section.

| Module | Landing page slug |
|---|---|
| AI Security | ai-security-best-practices-guide (already live, this is the v2 refresh) |
| CSPM | cspm-best-practices-guide |
| CWPP | cwpp-best-practices-guide |
| Kubernetes Security (KSPM) | kubernetes-security-best-practices-guide |
| ASPM | aspm-best-practices-guide |
| API Security | api-security-best-practices-guide |
| Secrets Management | secrets-management-best-practices-guide |
| CIEM | ciem-best-practices-guide |
| DSPM | dspm-best-practices-guide |
| Cloud Compliance | cloud-compliance-best-practices-guide |

Every landing page lives at `https://accuknox.com/cheatsheets/<slug>/`.

## Work Moves in Four Stages

1. Anish reviews the design.
2. Debjani Ma'am or Mrinal publishes the landing pages.
3. Kavitha sends the emails after a page is live.
4. Jahana posts on LinkedIn after a page is live.

Emails and posts link to the landing page, so they wait for stage 2. Stages 3 and 4 run in parallel.

## Anish Reviews the Design

Folder: `01 Design Review - Anish`

1. Open each module folder and read the PDF page by page.
2. Check the form image and the LinkedIn image in the same folder.
3. Reply in the Slack thread with a list of fixes per module, or "approved".
4. To edit a PDF yourself, unzip `editable-source-html.zip`. Each module folder holds `report.html`, its images and the Inter font. Send the changed HTML back to Atharva, who re-renders the PDF.

## Debjani Ma'am or Mrinal Publishes the Pages

Folder: `02 Website - Debjani and Mrinal`

1. Open the `Web page metadata` doc. It holds one block per page.
2. Duplicate the live AI security page at https://accuknox.com/cheatsheets/ai-security-best-practices-guide/ for each new page.
3. Set the title, meta title, meta description, slug, tagline, subtitle blurb and the five "What's inside" bullets from the doc.
4. Upload the module PDF behind the form, and put the form image beside the form.
5. Replace the AI security PDF and form image on the live page with the v4 files.
6. Submit each form once with a test email, and confirm the PDF arrives.
7. Post each live URL in the Slack thread.

## Kavitha Sends the Emails

Folder: `03 Emails - Kavitha`

1. Open the `Email copy` doc to review subject, preview text and body.
2. Import the matching `*-email.html` file into the email tool.
3. Wait for the website team to post the live URL, then test the button link.
4. Send a test email to yourself and check it on desktop and mobile.
5. Schedule the send and post the date in the Slack thread.

## Jahana Posts on LinkedIn

Folder: `04 Social - Jahana`

1. Open the `LinkedIn posts` doc.
2. Pair each post with its `*-linkedin.png` image.
3. Put the landing page link in the first comment, never in the post body.
4. Schedule one post per module after its page is live, and post the calendar in the Slack thread.

## Five Items Need a Check Before Launch

1. Secrets Management links to new Secrets Manager help pages that are not merged yet. Hold that page until Atharva confirms the docs are live.
2. CIEM and DSPM are labeled beta inside the PDFs, matching the product.
3. The CSPM closing page names Frost and Sullivan from the badge on accuknox.com/analyst-recognition. Confirm before publishing.
4. Every statistic in the PDFs, emails and posts carries its source. Do not change a number without checking that source.
5. Every PDF links to `accuknox.com/demo` with UTM tags, so demo bookings trace back to each cheat sheet.

## Files Outside Your Folder

`00 Start Here/LAUNCH-KIT.md` holds every package in one file. `accuknox-cheat-sheets-everything.zip` holds this whole folder.

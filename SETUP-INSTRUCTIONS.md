# 2026 Meal Calendar - Setup Instructions

## What's Been Created

Your `2026-meal-calendar` folder contains:

```
2026-meal-calendar/
├── github-pages/           ← Upload this folder to GitHub
│   ├── index.html          ← Main page with all weeks
│   ├── week-01.html        ← Week 1 recipes
│   ├── week-02.html        ← Week 2 recipes
│   ├── ... (52 weeks)
│   └── week-52.html        ← Week 52 recipes
│
├── printable/              ← Print these as PDFs
│   ├── shopping-week-01.html
│   ├── shopping-week-02.html
│   ├── ... (52 weeks)
│   └── shopping-week-52.html
│
├── january-2026.md         ← Detailed meal plans
├── february-2026.md
├── ... (12 months)
│
├── generate_pages.py       ← Script to regenerate recipe pages
├── generate_printable.py   ← Script to regenerate shopping lists
└── SETUP-INSTRUCTIONS.md   ← This file
```

---

## Step 1: Create a GitHub Account (if you don't have one)

1. Go to https://github.com
2. Click "Sign up"
3. Choose a username (e.g., `yourname-family`)
4. Complete the signup

---

## Step 2: Create a Repository for Your Meal Calendar

1. Log into GitHub
2. Click the **+** icon (top right) → **New repository**
3. Fill in:
   - Repository name: `2026-meal-calendar`
   - Description: `Family meal planning for 2026`
   - Select: **Public** (required for free GitHub Pages)
   - Check: **Add a README file**
4. Click **Create repository**

---

## Step 3: Upload Your Files

### Option A: Using GitHub Web Interface (Easiest)

1. Open your new repository on GitHub
2. Click **Add file** → **Upload files**
3. Open File Explorer and navigate to:
   `C:\Users\Little Nineveh\2026-meal-calendar\github-pages\`
4. Select ALL files in that folder (Ctrl+A)
5. Drag them into the GitHub upload area
6. Scroll down and click **Commit changes**

### Option B: Using GitHub Desktop (More Control)

1. Download GitHub Desktop: https://desktop.github.com
2. Clone your repository to your computer
3. Copy all files from `github-pages/` folder into the cloned folder
4. Commit and push

---

## Step 4: Enable GitHub Pages

1. In your repository, go to **Settings** (gear icon)
2. In the left sidebar, click **Pages**
3. Under "Source", select:
   - Branch: `main`
   - Folder: `/ (root)`
4. Click **Save**
5. Wait 1-2 minutes for the site to build
6. Your site will be live at:
   ```
   https://YOUR-USERNAME.github.io/2026-meal-calendar/
   ```

---

## Step 5: Update the QR Codes

Now that you have your GitHub Pages URL, you need to update the printable shopping lists:

1. Open the file:
   `C:\Users\Little Nineveh\2026-meal-calendar\generate_printable.py`

2. Find this line near the top:
   ```python
   BASE_URL = "https://YOUR-USERNAME.github.io/2026-meal-calendar"
   ```

3. Replace `YOUR-USERNAME` with your actual GitHub username

4. Save the file

5. Run the script again:
   - Open Command Prompt
   - Navigate to the folder:
     ```
     cd "C:\Users\Little Nineveh\2026-meal-calendar"
     ```
   - Run:
     ```
     py generate_printable.py
     ```

6. The QR codes in the printable files will now link to your live recipe pages!

---

## Step 6: Print Your Shopping Lists

1. Open each `shopping-week-XX.html` file in your browser
2. Press **Ctrl+P** to print
3. Select **Save as PDF** or print directly
4. Each sheet is designed to fit on A4 paper

### Batch Printing All 52 Weeks

You can open multiple HTML files and print them all at once, or convert them to PDF using your browser's print function.

---

## Testing Your Setup

1. Visit your GitHub Pages site:
   ```
   https://YOUR-USERNAME.github.io/2026-meal-calendar/
   ```

2. Click on "Week 1" to test a recipe page

3. Open a printable shopping list and scan the QR code with your phone

4. It should take you directly to that week's recipe page!

---

## Making Changes

### To update recipes:
1. Edit `generate_pages.py`
2. Re-run the script
3. Upload the new files to GitHub

### To update shopping lists:
1. Edit `generate_printable.py`
2. Re-run the script
3. Print the new versions

---

## Troubleshooting

**QR codes not working?**
- Make sure you updated the BASE_URL with your actual username
- Check that GitHub Pages is enabled and the site is live
- The URL must be exactly: `https://username.github.io/2026-meal-calendar`

**GitHub Pages not loading?**
- Wait a few minutes after enabling Pages
- Check that all files are in the root of the repository (not in a subfolder)
- Verify the `index.html` file was uploaded

**Can't see all 52 weeks?**
- Make sure you uploaded ALL files from the `github-pages/` folder

---

## Need Help?

- GitHub Pages docs: https://docs.github.com/en/pages
- GitHub Desktop: https://desktop.github.com

---

## Quick Reference

| What | Where |
|------|-------|
| Recipe pages to upload | `github-pages/` folder |
| Printable shopping lists | `printable/` folder |
| Monthly meal plans | `.md` files in main folder |
| Your live site | `https://YOUR-USERNAME.github.io/2026-meal-calendar/` |

# jmkozlik.github.io

My personal blog. Lives at **https://jmkozlik.github.io**.

## How to write a post (the whole workflow)

1. Create a file in `_posts/` named `YYYY-MM-DD-a-short-slug.md`
   — or just run `./new-post.sh "My Title"` and it makes one for you.
2. Write in Markdown under the front-matter block.
3. Publish:
   ```bash
   git add -A
   git commit -m "post: my title"
   git push
   ```
4. GitHub rebuilds the site automatically. It's live in under a minute at
   your URL. No servers, no build commands.

## Renaming the blog

Edit the top three lines of `_config.yml` (`title`, `description`, `author`),
commit, and push.

## Changing the look

All styling is in `assets/style.css`. The colors and fonts are CSS variables
at the very top of that file — change those to restyle the whole site. It's
built to work in both light and dark mode automatically.

## Previewing locally (optional — you don't need this)

You only need this if you want to see changes before pushing. GitHub builds
the real site for you regardless.

```bash
bundle install        # first time only
bundle exec jekyll serve
# then open http://localhost:4000
```

## Layout

```
_config.yml          site title/description + build settings
index.html           the homepage (lists your posts)
about.md             the About page
_posts/              one Markdown file per post
_layouts/            page templates (default, post)
assets/style.css     all the styling
feed.xml             RSS/Atom feed (auto-generated)
new-post.sh          helper to create a new post file
```

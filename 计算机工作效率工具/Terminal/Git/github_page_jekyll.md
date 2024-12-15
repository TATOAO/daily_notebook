

# install jekyll

gem install bundler jekyll

# jekyll create project

```
# new project
jekyll new new_project_directory_name
# existed project
jekyll new . --force
```

# serve jekyll (dev)

```
bundle exec jekyll serve
```

# jekyll build

```
jekyll build
```


# explain
Ah, I see where the confusion is coming from! To clarify: **GitHub Pages does not automatically generate the `_site/` folder for you**. Let me explain how it works when you're using GitHub Pages and Jekyll:

### **How GitHub Pages Works with Jekyll**

When you push your Jekyll project to GitHub (and set up GitHub Pages), GitHub **does automatically run the Jekyll build process** for you in the background to generate the site. However, this happens **on GitHub's servers**, not on your local machine, and the generated files are not stored in the repository itself.

Here’s what happens in detail:

1. **GitHub Pages Builds the Site**:
   - When you push your Jekyll project to GitHub, if you've set up GitHub Pages to serve from your `main` branch (or a custom branch like `gh-pages`), GitHub will run `jekyll build` on their servers to generate the static files.
   - This means GitHub will generate the `_site/` folder **on their servers**, not in your local project. So, you **won't see the `_site/` folder in your GitHub repository** (because it's not part of the code repository—it's only part of the build process).
   
2. **No Need to Commit the `_site/` Folder**:
   - Since GitHub generates the site for you, you don't need to commit or push the `_site/` folder into your repository. This is why the `_site/` folder is ignored by default in `.gitignore`.
   - When you visit your GitHub Pages site (e.g., `username.github.io` or a custom domain), GitHub is serving the generated static files from the `_site/` folder they created during the build process.

3. **What You Push to GitHub**:
   - You only need to push the source files (like your `_posts`, `_layouts`, and other assets), not the contents of `_site/`.
   - After pushing these files to GitHub, the platform will automatically rebuild the site and deploy the results.
   
4. **Where Does the Generated Site Go?**
   - GitHub Pages will automatically take the output from `_site/` and make it available to the public via your GitHub Pages URL, but **you will not see these files in the repository** unless you specifically push them to a branch like `gh-pages` or to a folder like `/docs` (if you're using a custom setup).
   - If you're using GitHub Pages in a typical setup (deploying from `main`), you won't see `_site/` in the GitHub repository, because GitHub Pages is handling the generation and deployment process for you.

### **What GitHub Does Not Do**
- GitHub Pages does not automatically sync the files from your local `_site/` directory. You need to push the source files (like `.md`, `.html`, etc.) to your GitHub repository, and GitHub will build the site when you visit the GitHub Pages URL.
  
### **Where Are the Generated Files?**
- **On your GitHub Pages site**, not in the repository.
- **In the background on GitHub servers**, but you won't see those files in your GitHub repo unless you decide to manually push them (e.g., for a custom `gh-pages` deployment).

### **How Can You Use GitHub Pages with Jekyll (Typical Workflow)?**

1. Push your Jekyll site to GitHub (including all the source files, not `_site/`).
2. Set up GitHub Pages to serve the site from the `main` branch (or `gh-pages`, depending on your setup).
3. GitHub Pages automatically builds the static files and serves them from a URL like `username.github.io`.
4. You don't need to push the `_site/` folder, as GitHub will handle it for you.

### **If You Want to Manually Push the `_site/` Folder**
If you want more control over the deployment process (for example, if you're using a custom deployment branch like `gh-pages`), you can manually push the `_site/` folder. However, this is not required for most GitHub Pages setups because GitHub handles the build process for you.

To summarize:

- GitHub Pages **does build the site for you**, but you won’t see the `_site/` folder in the repository because it is generated on GitHub’s servers during the build process.
- **You don’t need to commit the `_site/` folder** to Git because GitHub Pages automatically generates and deploys the site from the files you push (the source files).
- The `_site/` folder is where the generated static files are stored locally on your machine, but it's ignored by Git because it's not needed for version control or deployment.

Let me know if that clears things up!


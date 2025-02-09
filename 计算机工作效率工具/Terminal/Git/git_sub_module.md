To convert a directory in your existing Git repository into a Git submodule, follow these steps:

---

### **1. Split the Directory into a Standalone Repository**
**Goal:** Preserve the directory's history in a new repository.

1. **Clone your original repository** (to avoid altering the original directly):
   ```bash
   git clone original-repo-url split-repo
   cd split-repo
   ```

2. **Use `git filter-repo`** to extract the directory's history into a new repo:
   ```bash
   # Install git-filter-repo if not already installed
   # pip install git-filter-repo

   git filter-repo --subdirectory-filter path/to/directory
   ```
   - This moves the contents of `path/to/directory` to the root of the new repository and removes all other files.

3. **Push the new repository to GitHub**:
   ```bash
   git remote add origin git@github.com:username/new-submodule-repo.git
   git push -u origin main
   ```

---

### **2. Remove the Directory from the Original Repository**
**Goal:** Clean the original repository of the directory and its history.

1. **Navigate back to your original repository**:
   ```bash
   cd /path/to/original-repo
   ```

2. **Remove the directory and its history**:
   ```bash
   git filter-repo --path path/to/directory --invert-paths
   ```
   - This removes all traces of `path/to/directory` from the repository's history.

3. **Push the cleaned history to GitHub** (force-push if necessary):
   ```bash
   git push origin main --force
   ```
   ⚠️ **Warning:** Force-pushing rewrites history. Coordinate with collaborators to avoid conflicts.

---

### **3. Add the New Repository as a Submodule**
**Goal:** Link the new standalone repository as a submodule in the original directory's location.

1. **Add the submodule**:
   ```bash
   git submodule add git@github.com:username/new-submodule-repo.git path/to/directory
   ```

2. **Commit and push the changes**:
   ```bash
   git commit -m "chore: add submodule for path/to/directory"
   git push origin main
   ```

---

### **4. Final Steps**
- **Cloning the main repository**:
  Users will need to initialize and update submodules:
  ```bash
  git clone --recurse-submodules original-repo-url
  # OR after cloning:
  git submodule update --init --recursive
  ```
  同步所有的子project

- **Updating the submodule**:
  Changes in the submodule must be committed and pushed separately in its own repository.

---

### **Troubleshooting**
- **Error: "Directory already exists"** when adding a submodule:
  - Temporarily move the directory out of the main repo:
    ```bash
    mv path/to/directory /tmp/directory-backup
    git submodule add ...  # Add submodule
    mv /tmp/directory-backup/* path/to/directory/
    rm -rf /tmp/directory-backup
    ```

- **Collaborators must re-clone**:
  After rewriting history, collaborators should:
  ```bash
  git fetch origin
  git reset --hard origin/main
  git submodule update --init --recursive
  ```

---

This workflow preserves the directory's history in the submodule while cleaning the main repository. Let me know if you need further clarification!

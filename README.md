Points to note
==============

Bring up problems early, don't wait till the weekly meeting.

Use @ mention to tag someone to help look at the problem.

Always create an issue+commits for something you've spent time on.


General workflow
================

Create issues for things to be done.

Discuss issues using comments, use @ mention to tag others to join in the
dicussion.

Push commits to address issues.
  every commit message must reference some issue
  e.g. "fix array out of bugs, for #52"

Use @ mention to get review and remember to assign issue to reviewer.

Reviewer to close and reassign back to committer.

Using git
=========

Version control is done with git.

As commits are mainly done by one person, commits should be pushed to master directly. No need for branches.

Merge commits are to be avoided by rebasing commits on top of current master.

The following settings in gitconfig does this automatically when you pull:

```
[pull]
    rebase = true
[rebase]
    autoStash = true
```

Using snakemake
===============

Running of programs to generate output is done with Snakemake.

The rules are written in Snakefile.

Running `snakemake` will execute the first rule.

Running `snakemake <output>` will attempt to generate the particular output file, eg `snakemake report.pdf`.

Running `snakemake <rule>` will execute the given rule in the Snakefile.

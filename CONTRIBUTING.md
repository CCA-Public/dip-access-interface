# Contributing

Thank you for considering a contribution!
This document outlines the change submission process, along with our standards for new code contributions.
Following these guidelines helps us assess your changes faster and makes it easier for us to merge your submission!

**Table of Contents**

- [Submitting bugs](#submitting-bugs)
- [Submitting enhancement ideas](#submitting-enhancements)
- [Submitting code changes](#submitting-code-changes)
  - [Getting started](#getting-started)
  - [When to submit code for review?](#when-to-submit-code-for-review)
  - [Opening the pull request](#opening-the-pull-request)
  - [Discussion](#discussion)
  - [Cleaning up the commit history](#cleaning-up-the-commit-history)
- [Contribution standards](#contribution-standards)
  - [Style](#style)
    - [Some extra notes](#some-extra-notes)
    - [Exceptions](#exceptions)
    - [Working with legacy code](#working-with-legacy-code)
  - [Documentation](#documentation)
  - [Tests](#tests)
  - [Commit History](#commit-history)
    - [Commits should be specific and atomic](#commits-should-be-specific-and-atomic)
    - [Every commit should work](#every-commit-should-work)
    - [Commit summaries should be concise](#commit-summaries-should-be-concise)
    - [Commit messages should be as detailed as they need to be (and no more)](#commit-messages-should-be-as-detailed-as-they-need-to-be-and-no-more)
 - [Code of Conduct](#code-of-conduct)

## Submitting bugs

Issues can be filed using GitHub Issues in the
[Issues repo](https://github.com/CCA-Public/scope/issues). It is
recommended to file issues there rather than in any of the Archivematica-related
code repositories. CCA and Artefactual staff also use GitHub issues for any work they do
on this project.

Useful questions to answer if you're having problems include:

* What version of Archivematica and the Storage Service are you using?
* How was Archivematica installed? Package install, Ansible, etc?
* What version of SCOPE are you using?
* Was this a fresh install or an upgrade?
* What did you do to cause this bug to happen?
* What did you expect to happen?
* What did you see instead?
* Can you reproduce this reliably?
* If a specific Job is failing, what output did it produce? This is available by clicking on the gear icon.

## Submitting enhancement ideas

Similar to submitting bugs, you are welcome to submit ideas for enhancements or
new features in the
[Issues repo](https://github.com/CCA-Public/scope/issues). This is
also where Artefactual and CCA staff record upcoming enhancements when they have been
sponsored for inclusion.

## Submitting code changes

Every new feature and bugfix to a project is expected to go through code review before inclusion.
This applies both to developers at CCA and to outside contributors.

Here's an outline of the contribution process:

1. File an issue in the
   [Issues repo](https://github.com/CCA-Public/scope/issues).
2. Fork the project on GitHub, and commit your changes to a branch
   in your fork.
3. Open a pull request.
4. Back and forth discussion with developers on the branch.
5. Make any changes suggested by reviewers.
6. Repeat 3 and 4 as necessary.
7. Clean up commit history, if necessary.
8. Your branch will be merged!

### Getting started

So you have something to contribute to SCOPE. Great!

To install SCOPE, see our [development installation](https://github.com/CCA-Public/scope#installation) instructions.

CCA uses [GitHub](https://github.com/)'s pull request feature for code review.
Every change being submitted to an SCOPE should be submitted as a pull request to the appropriate repository.
A branch being submitted for code review should contain commits covering a related section of code.
Try not to bundle unrelated changes together in one branch; it makes review harder.

If you're not familiar with forking repositories and creating branches in GitHub, consult their [guide](https://help.github.com/articles/fork-a-repo).

### When to submit code for review?

Your code doesn't have to be ready yet to submit for code review!
You should submit a branch for code review as soon as you want to get feedback on it.
Sometimes, that means submitting a feature-complete branch, but sometimes that means submitting an early WIP in order to get feedback on direction.
Don't be shy about submitting early.

### Opening the pull request

GitHub has an [excellent guide](https://help.github.com/articles/using-pull-requests) on using the pull request feature.

### Discussion

Discussion on pull requests is usually a back and forth process.
Don't feel like you have to make every change the reviewer suggests; the pull request is a great place to have in-depth conversation on the issue.

Do make use of GitHub's line comment feature!

![Line comment](http://i.imgur.com/FsWppGN.png)

By viewing the "Files changed", you can leave a comment on any line of the diff.
This is a great way to scope discussion to a particular part of a diff.
Any discussion you have in a specific part of the diff will also be automatically hidden once a change is pushed that addresses it, which helps keep the pull request page clear and readable.

Anyone can participate in code review discussions.
Feel free to jump in if you have something to contribute on another pull request, even if you're not the one who opened it.

### Cleaning up the commit history

Once code review is finished or nearly finished, and no further development is planned on the branch, the branch's commit history should be cleaned up.
You can alter the commit history of a branch using git's powerful [interactive rebase feature](http://www.git-scm.com/book/en/Git-Tools-Rewriting-History).

## Contribution standards

### Style

SCOPE uses the Python [PEP8](https://www.python.org/dev/peps/pep-0008/) community style guidelines.
Newly-written code should conform to PEP-8 style.
PEP8 is a daunting document, but there are very good linters available that you can run to check style in your code.
The [flake8](https://pypi.python.org/pypi/flake8) tool checks for style problems as well as errors and complexity.
It can be used at the command line or as a plugin in your preferred text editor/IDE.

#### Some extra notes

A few additional stylistic preferences might not get flagged by linters:

* Don't use variable or parameter names that shadow builtin functions and types.
  For example, don't name a variable "file".
  (Unfortunately, Python uses many useful names for its builtin types and functions.)
* Sort imports alphabetically within their grouping to reduce duplicate imports.

#### Exceptions

SCOPE ignores the PEP8 rule concerning line length; lines longer than 80 characters are acceptable.
This is error "501", for the purposes of silencing it in flake8 or other linting tools.

#### Working with legacy code

Older portions of the codebase don't always conform to PEP8 rules; the codebase is slowly transitioning to PEP8 style.
Don't worry about rewriting existing code to conform to the guidelines when adding new code; however, if possible, it's great if your new code does conform.

When working in sections of code that don't conform to PEP8, it's okay to relax a few PEP8 rules in order to match existing code.
In particular:

* When modifying an existing function which uses camelCase variables or parameters, it's okay to make your new variables/parameters camelCase to match.
* When adding new functions to a module or class that uses camelCase naming, it's okay to make your new function and its parameters camelCase to match.
  Try to use snake_case internally, however.

You should try to write Python 2 / Python 3 compatible code where possible.
Using `from __future__ import print_function, division, absolute_import` will help with this.
Some libraries run in Python 2 and Python 3 already; this behaviour should be maintained.

### Documentation

New classes and functions should generally be documented using [docstrings](https://en.wikipedia.org/wiki/Docstring#Python); these help in providing clarity, and can also be used to generate API documentation later.
Generally any function which isn't obvious (any function longer than a line or two) should have a docstring.
When in doubt: document!
Python's [PEP 257](https://www.python.org/dev/peps/pep-0257/) document provides a useful guideline for docstring style.
Generally, prefer using [Sphinx-compatible docstrings](http://pythonhosted.org/an_example_pypi_project/sphinx.html#function-definitions).
More [examples](http://sphinx-doc.org/domains.html#info-field-lists) and [attributes to use](http://sphinx-doc.org/domains.html#the-python-domain) can be found on the Sphinx website.

### Tests

New code should also have unit tests.
Tests are written in [unittest](https://docs.python.org/2/library/unittest.html) style and run with [py.test](http://pytest.org).
For tests requiring the Django ORM, we use the Django-provided [TestCase](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.TestCase), which extends `unittest.TestCase`.

Tests are found in the `tests` directory, a sibling of the directory containing the code.
`test_foo.py` contains tests for `foo.py`.
For clarity, group tests for the same function and similar tests into the same class within that file.
This will also allow you to share setup and teardown code.

If you are testing code that makes HTTP requests, using [VCR.py](https://github.com/kevin1024/vcrpy) is highly recommended.
It should already be a development dependency.

### Commit History

A clean commit history makes it easier to see what changes are related, and why there were made.
It makes reviewing code easier, and spelunking in the codebase to find why a change was made more rewarding.
The following few criteria help outline what makes for a clean commit history:

#### Commits should be specific and atomic

Any single commit should cover a specific change.
That change might span multiple files, but it shouldn't introduce multiple distinct functional changes unless it's impossible to separate those changes from each other.
It's okay (and normal!) for a branch that makes a lot of changes to consist of many small commits, each of which makes individual small changes.
This makes it easier to revert individual commits from a branch, and also makes it easier to isolate the commit that caused a particular bug with git-blame.

In development, it's common to introduce a change with a commit and then introduce multiple other commits with small fixes for that change.
When getting ready for merging, those commits should all be squashed together.

#### Every commit should work

No individual commit should put the software in a broken state.
It's fine for code to go unused (because the feature it's been introduced for isn't there yet), but no new functional issues should be introduced by a given commit.
This ensures that reverting any individual commit from the branch is safe, and that git-bisect stays reliable for tracking down bugs.

#### Commit summaries should be concise

The commit summary (the first line of a commit message) should be short and clear.
Usually, the first line of the commit message should be 50 - 80 characters.
Since the summary is just a *summary* of the change, it should be readable at a glance when looking through git history.

A good commit summary makes it clear a) what *part* of the code is changing, and b) what the change is.
For example:

Clear commit summary:
> normalize: fall back to default rule for unidentified files

Unclear commit summaries:
> Fixed some normalization bugs

> Bugfixes

The unclear messages make it hard to tell at a glance what changed, and that makes browsing the commit history harder.

#### Commit messages should be as detailed as they need to be (and no more)

The commit message is the rest of the commit past the first line.
If a commit makes a small and obvious change, it's fine to not even have a commit message past the summary.

The commit message is your place to clarify the justification for a change.
While there's no need to rehash anything that code comments already say, if
there's more detail that helps a reader understand *why* a change was made, be
as verbose as you need to! Remember: future-you (or another developer) will
read this when going through the commit history to understand why a change was
made. Make their life easier.

Each line of a commit message should be no more than 72 characters in width.
The following is an outline of a commit message combined with an ideal commit
summary:
```
Capitalized, short (50 chars or less) summary

More detailed explanatory text, if necessary.  Wrap it to about 80
characters or so.  In some contexts, the first line is treated as the
subject of an email and the rest of the text as the body.  The blank
line separating the summary from the body is critical (unless you omit
the body entirely); tools like rebase can get confused if you run the
two together.

Further content comes after a blank line.
```
##### More information on commit messages
For more information about how to write a good commit message and to
understand some of the rationale behind our approach, please see this
article from Chris Beams on
[How to write a Git commit message](https://chris.beams.io/posts/git-commit/).

## Code of Conduct
SCOPE is dedicated to providing a harassment-free experience for everyone, regardless of gender, gender identity and expression, sexual orientation, disability, physical appearance, body size, age, race, or religion. We do not tolerate harassment of participants in any form.

This code of conduct applies to all SCOPE-related spaces, including the Github repository, both online and off. Anyone who violates this code of conduct may be sanctioned or expelled from these spaces at the discretion of the project team.

Derived from [Geek Feminism's anti-harassment policy](http://geekfeminism.wikia.com/wiki/Community_anti-harassment/Policy).

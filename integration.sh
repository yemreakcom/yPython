python ../YGitBookIntegration/integrate.py . -ll 1
echo "---
description: Sitede neler olup bittiğinin raporudur.
---" > CHANGELOG.md
ygitchangelog -d >> CHANGELOG.md
bash github

python ../YGitBookIntegration/integrate.py .
echo "---
description: Sitede neler olup bittiğinin raporudur.
---" > CHANGELOG.md
gitchangelog -d >> CHANGELOG.md
gbash github

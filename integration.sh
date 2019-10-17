python ../YGitBookIntegration/integrate.py . -ll 1 -l ../YWiki/Programlama\ Notları/Python/README.md -u https://python.yemreak.com
echo "---
description: Sitede neler olup bittiğinin raporudur.
---" > CHANGELOG.md
ygitchangelog -d >> CHANGELOG.md
bash github

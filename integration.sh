python ../YGitBookIntegration/integrate.py . -ll 1 -l ../YWiki/1\ -\ Programlama\ Notları/1\ -\ Python/README.md -u https://python.yemreak.com
echo "---
description: Sitede neler olup bittiğinin raporudur.
---" > CHANGELOG.md
ygitchangelog -d >> CHANGELOG.md
bash github

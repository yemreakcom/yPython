# Geliştiriciler için Notlar

## Encoded Çözümü

- `"%USERPROFILE%\appdata\local\programs\python\python37\lib\site-packages\gitchangelog\gitchangelog.py"`
- [Encode sorunu çözümü](https://github.com/yedhrab/gitchangelog/commit/6f186595ed125b2d08d73b76ad98b572684e7506)

> [Sorunsuz repo](https://github.com/yedhrab/gitchangelog)

## Changelog Yapısı

| Özellik          | RegEx                                                                                                                                              |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `🚀 Yenilikler`  | `r'\bekle|\boluş|(\byeni )|\b[cC]reate|\barttır|\bartır'`                                                                                          |
| `🌌 Değişiklik`  | `r'\btaşı|\bdeğiş|\b[uU]pdate|\bgüncel|\byenile|\bdönül|\bgeç|\bkoyu|\byapılan|\b[rR]evert|\b[gG]eri|\balındı|\baktar|\byenile|(\bevril)|\bgetir'` |
| `🗽 Düzeltmeler` | `r'\b[bB]ug|\bdüzen|\bdüzelt|\bgider|\bkalk|\b[kK]aldır|\bayrıl|\b[dD]elete'`                                                                      |
| `'📡 Diğerler'`  | Geri kalanlar                                                                                                                                      |

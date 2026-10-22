# Сайт Level Marketing + агент-контентщик

- `site.json` — название, адрес сайта, контакты (Telegram, телефон, Instagram).
- `content/uz/blog/`, `content/ru/blog/` — статьи и кейсы (Markdown).
- `build.py` — собирает сайт в `docs/` (только стандартный Python, без установки пакетов).
- `agent/AGENT.md` — инструкция агента; `agent/topics.md` — темы; `agent/cases-inbox/` — сюда кладёте кейсы; `agent/log.md` — что агент сделал.

Проверить локально:

```bash
python3 build.py && cd docs && python3 -m http.server 8765
```

## Хостинг: GitHub Pages

- `build.py` собирает сайт в папку `docs/`, она коммитится вместе со статьями.
- GitHub Pages раздаёт `docs/` из ветки `main`: Settings → Pages → Deploy from a branch → `main` / `/docs`.
- Адрес: https://azizbekmukhitdinov-afk.github.io/level-marketing-site/ (он же `url` в `site.json`).
- Каждый `git push` агента → сайт обновляется сам за 1–2 минуты.

**Свой домен.** Купите домен, в Settings → Pages → Custom domain впишите его, у регистратора добавьте DNS-записи, которые покажет GitHub, и поменяйте `url` в `site.json` на `https://<домен>` (без пути).

**Поисковики.** Добавьте сайт в Google Search Console и Яндекс Вебмастер, отправьте `sitemap.xml`. Заполните профиль компании в Google и Яндекс Картах со ссылкой на сайт.

## Ежедневная работа агента

Агент — запланированная задача в приложении Claude (раздел Scheduled). Каждый день в 09:00 он читает `agent/AGENT.md`, выбирает тему, пишет статью на узбекском и русском, собирает сайт и делает `git push`.

Условия: Mac включён, не спит, приложение Claude открыто. Отчёт о каждой смене — в `agent/log.md`.

Что делаете вы:
- кладёте реальные кейсы в `agent/cases-inbox/` по шаблону `_SHABLON.md` (только с разрешения клиента);
- при желании вписываете свои темы в начало `agent/topics.md`;
- раз в неделю просматриваете новые статьи.

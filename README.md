# Сайт Level Marketing + агент-контентщик

- `site.json` — название, адрес сайта, контакты (Telegram, телефон, Instagram).
- `content/uz/blog/`, `content/ru/blog/` — статьи и кейсы (Markdown).
- `build.py` — собирает сайт в `dist/` (только стандартный Python, без установки пакетов).
- `agent/AGENT.md` — инструкция агента; `agent/topics.md` — темы; `agent/cases-inbox/` — сюда кладёте кейсы; `agent/log.md` — что агент сделал.

Проверить локально:

```bash
python3 build.py && cd dist && python3 -m http.server 8765
```

## Запуск в интернет (один раз)

1. **Контакты.** Впишите в `site.json` Telegram (без @), телефон и Instagram — на них ведут все кнопки «Bepul audit olish».
2. **GitHub.** Создайте приватный репозиторий `level-marketing-site` на github.com (пустой, без README). Затем в папке сайта:
   ```bash
   git remote add origin https://github.com/<ваш-логин>/level-marketing-site.git
   git push -u origin main
   ```
   При первом push macOS спросит логин и токен GitHub (Settings → Developer settings → Personal access tokens → *Fine-grained*, доступ Contents: Read and write к этому репозиторию). После этого агент сможет пушить сам.
3. **Cloudflare Pages.** dash.cloudflare.com → Workers & Pages → Create → Pages → Connect to Git → выбрать репозиторий.
   - Project name: `level-marketing` (тогда адрес будет `level-marketing.pages.dev`, как в `site.json`)
   - Build command: `python3 build.py`
   - Build output directory: `dist`
   Каждый push агента → сайт обновляется сам за 1–2 минуты.
4. **Домен.** Купите домен (например, `.uz` у uz-регистратора или `.com`), подключите его в Cloudflare Pages → Custom domains и поменяйте `url` в `site.json` на новый адрес.
5. **Поисковики.** Добавьте сайт в Google Search Console и Яндекс Вебмастер, отправьте `https://<домен>/sitemap.xml`. Создайте профиль компании в Google Картах и Яндекс Картах со ссылкой на сайт.

## Ежедневная работа агента

Агент — запланированная задача в приложении Claude (раздел Scheduled). Каждый день в 09:00 он читает `agent/AGENT.md`, выбирает тему, пишет статью на узбекском и русском, собирает сайт и делает `git push`.

Условия: Mac включён, не спит, приложение Claude открыто. Отчёт о каждой смене — в `agent/log.md`.

Что делаете вы:
- кладёте реальные кейсы в `agent/cases-inbox/` по шаблону `_SHABLON.md` (только с разрешения клиента);
- при желании вписываете свои темы в начало `agent/topics.md`;
- раз в неделю просматриваете новые статьи.

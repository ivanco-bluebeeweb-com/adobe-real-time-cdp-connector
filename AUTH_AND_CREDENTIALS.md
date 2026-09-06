# Adobe Real-Time CDP Connector — Auth & Credentials Standard

**Compliance:** AUTH_AND_CREDENTIALS_STANDARD.md (B1–B10)

## Схема аутентификации
- **Метод:** Adobe IMS OAuth 2.0 (Server-to-Server) + x-api-key + x-gw-ims-org-id
- **Хранение:** Секреты сохраняются изолированно в хранилище секретов платформы Imperal.
- **Валидация:** При сохранении ключа выполняется тестовый запрос `GET /data/foundation/catalog/datasets`.
- **Отключение:** Удаление локальных ключей без воздействия на аккаунт вендора.

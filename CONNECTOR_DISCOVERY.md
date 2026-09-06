# Adobe Real-Time CDP Connector — Discovery

**Vendor:** Adobe Real-Time CDP (https://business.adobe.com/products/experience-platform/real-time-customer-data-platform.html)  
**API Base URL:** `https://platform.adobe.io`  
**Authentication:** Adobe IMS OAuth 2.0 (Server-to-Server) + x-api-key + x-gw-ims-org-id

## Архитектура API
- **Ключевые сущности:** Real-Time Customer Profile, схемы XDM (/schemaregistry), каталоги датасетов (/data/foundation/catalog), определения сегментов
- **Формат обмена данными:** JSON / HTTPS REST.
- **Обработка ошибок:** Стандартные HTTP-коды (400, 401, 403, 404, 429, 500) с типизацией ответа.
- **Тестовая точка проверки подключения:** `GET /data/foundation/catalog/datasets`.

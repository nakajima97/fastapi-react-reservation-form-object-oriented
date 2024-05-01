```mermaid
erDiagram
  reservations {
    bigint id PK
    date date
    string name
    string email_address
    string phone_number
    datetime created_at
    datetime updated_at
  }

  calendars {
    bigint id PK
    date date UK
    tinyint is_holiday
    datetime created_at
    datetime updated_at
  }
```
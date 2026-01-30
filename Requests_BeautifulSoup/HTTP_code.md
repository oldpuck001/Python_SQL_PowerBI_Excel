HTTP_code.md

常見的 HTTP 狀態碼及其含義

- 200 OK: 請求成功。如果沒有收到這個狀態碼，表示請求沒有完全成功。

- 301 Moved Permanently 或 302 Found: 請求的資源被永久移動或臨時移動到了新的 URL。這通常不表示登錄失敗，但可能需要你的程序跟蹤重定向。

- 400 Bad Request: 服務器無法理解請求格式，請求有誤。

- 401 Unauthorized: 請求未經授權。通常是因為沒有提供正確的認證信息。

- 403 Forbidden: 服務器拒絕執行。即使有有效的認證信息，也無權訪問資源。

- 404 Not Found: 找不到請求的資源。

- 500 Internal Server Error: 服務器遇到錯誤，無法完成請求。

- 502 Bad Gateway 503 Service Unavailable 或 504 Gateway Timeout: 服務器作為網關或代理，從上游服務器收到無效響應。
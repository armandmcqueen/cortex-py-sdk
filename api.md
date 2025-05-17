# API

## Infra

### LockedRoom

Types:

```python
from cortexsdk.types.api.infra import LockedRoomAdminRoomResponse, LockedRoomUserRoomResponse
```

Methods:

- <code title="get /api/infra/locked-room/admin">client.api.infra.locked_room.<a href="./src/cortexsdk/resources/api/infra/locked_room.py">admin_room</a>() -> <a href="./src/cortexsdk/types/api/infra/locked_room_admin_room_response.py">object</a></code>
- <code title="get /api/infra/locked-room/user">client.api.infra.locked_room.<a href="./src/cortexsdk/resources/api/infra/locked_room.py">user_room</a>() -> <a href="./src/cortexsdk/types/api/infra/locked_room_user_room_response.py">object</a></code>

### Apikey

Types:

```python
from cortexsdk.types.api.infra import ApikeyCreateResponse, ApikeyListResponse, ApikeyDeleteResponse
```

Methods:

- <code title="post /api/infra/apikey">client.api.infra.apikey.<a href="./src/cortexsdk/resources/api/infra/apikey.py">create</a>(\*\*<a href="src/cortexsdk/types/api/infra/apikey_create_params.py">params</a>) -> <a href="./src/cortexsdk/types/api/infra/apikey_create_response.py">ApikeyCreateResponse</a></code>
- <code title="get /api/infra/apikey">client.api.infra.apikey.<a href="./src/cortexsdk/resources/api/infra/apikey.py">list</a>() -> <a href="./src/cortexsdk/types/api/infra/apikey_list_response.py">ApikeyListResponse</a></code>
- <code title="delete /api/infra/apikey/{token}">client.api.infra.apikey.<a href="./src/cortexsdk/resources/api/infra/apikey.py">delete</a>(token) -> <a href="./src/cortexsdk/types/api/infra/apikey_delete_response.py">object</a></code>

### User

Types:

```python
from cortexsdk.types.api.infra import User, UserListResponse, UserDeleteResponse
```

Methods:

- <code title="post /api/infra/user">client.api.infra.user.<a href="./src/cortexsdk/resources/api/infra/user.py">create</a>(\*\*<a href="src/cortexsdk/types/api/infra/user_create_params.py">params</a>) -> <a href="./src/cortexsdk/types/api/infra/user.py">User</a></code>
- <code title="get /api/infra/user/{user_id}">client.api.infra.user.<a href="./src/cortexsdk/resources/api/infra/user.py">retrieve</a>(user_id) -> <a href="./src/cortexsdk/types/api/infra/user.py">User</a></code>
- <code title="get /api/infra/user">client.api.infra.user.<a href="./src/cortexsdk/resources/api/infra/user.py">list</a>() -> <a href="./src/cortexsdk/types/api/infra/user_list_response.py">UserListResponse</a></code>
- <code title="delete /api/infra/user/{user_id}">client.api.infra.user.<a href="./src/cortexsdk/resources/api/infra/user.py">delete</a>(user_id) -> <a href="./src/cortexsdk/types/api/infra/user_delete_response.py">object</a></code>

## Experiments

Types:

```python
from cortexsdk.types.api import ExperimentHealthCheckResponse
```

Methods:

- <code title="get /api/experiments/health">client.api.experiments.<a href="./src/cortexsdk/resources/api/experiments.py">health_check</a>() -> <a href="./src/cortexsdk/types/api/experiment_health_check_response.py">object</a></code>

## Public

Types:

```python
from cortexsdk.types.api import PublicPublicRoomResponse, PublicWhoamiResponse
```

Methods:

- <code title="get /api/public/room">client.api.public.<a href="./src/cortexsdk/resources/api/public.py">public_room</a>() -> <a href="./src/cortexsdk/types/api/public_public_room_response.py">object</a></code>
- <code title="get /api/public/whoami">client.api.public.<a href="./src/cortexsdk/resources/api/public.py">whoami</a>() -> <a href="./src/cortexsdk/types/api/public_whoami_response.py">object</a></code>

## Books

Types:

```python
from cortexsdk.types.api import BookUploadEpubResponse
```

Methods:

- <code title="post /api/books/epub/upload">client.api.books.<a href="./src/cortexsdk/resources/api/books.py">upload_epub</a>(\*\*<a href="src/cortexsdk/types/api/book_upload_epub_params.py">params</a>) -> <a href="./src/cortexsdk/types/api/book_upload_epub_response.py">object</a></code>

# Healthz

Types:

```python
from cortexsdk.types import HealthzCheckResponse
```

Methods:

- <code title="get /healthz">client.healthz.<a href="./src/cortexsdk/resources/healthz.py">check</a>() -> <a href="./src/cortexsdk/types/healthz_check_response.py">HealthzCheckResponse</a></code>

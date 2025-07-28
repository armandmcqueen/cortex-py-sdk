# API

## Infra

### LockedRoom

Methods:

- <code title="get /api/infra/locked-room/admin">client.api.infra.locked_room.<a href="./src/cortexsdk/resources/api/infra/locked_room.py">retrieve_admin</a>() -> object</code>
- <code title="get /api/infra/locked-room/user">client.api.infra.locked_room.<a href="./src/cortexsdk/resources/api/infra/locked_room.py">retrieve_user</a>() -> object</code>

### Apikey

Types:

```python
from cortexsdk.types.api.infra import ApikeyCreateResponse, ApikeyListResponse
```

Methods:

- <code title="post /api/infra/apikey">client.api.infra.apikey.<a href="./src/cortexsdk/resources/api/infra/apikey.py">create</a>(\*\*<a href="src/cortexsdk/types/api/infra/apikey_create_params.py">params</a>) -> <a href="./src/cortexsdk/types/api/infra/apikey_create_response.py">ApikeyCreateResponse</a></code>
- <code title="get /api/infra/apikey">client.api.infra.apikey.<a href="./src/cortexsdk/resources/api/infra/apikey.py">list</a>() -> <a href="./src/cortexsdk/types/api/infra/apikey_list_response.py">ApikeyListResponse</a></code>
- <code title="delete /api/infra/apikey/{token}">client.api.infra.apikey.<a href="./src/cortexsdk/resources/api/infra/apikey.py">delete</a>(token) -> object</code>

### User

Types:

```python
from cortexsdk.types.api.infra import User, UserListResponse
```

Methods:

- <code title="post /api/infra/user">client.api.infra.user.<a href="./src/cortexsdk/resources/api/infra/user.py">create</a>(\*\*<a href="src/cortexsdk/types/api/infra/user_create_params.py">params</a>) -> <a href="./src/cortexsdk/types/api/infra/user.py">User</a></code>
- <code title="get /api/infra/user/{user_id}">client.api.infra.user.<a href="./src/cortexsdk/resources/api/infra/user.py">retrieve</a>(user_id) -> <a href="./src/cortexsdk/types/api/infra/user.py">User</a></code>
- <code title="get /api/infra/user">client.api.infra.user.<a href="./src/cortexsdk/resources/api/infra/user.py">list</a>() -> <a href="./src/cortexsdk/types/api/infra/user_list_response.py">UserListResponse</a></code>
- <code title="delete /api/infra/user/{user_id}">client.api.infra.user.<a href="./src/cortexsdk/resources/api/infra/user.py">delete</a>(user_id) -> object</code>

## Experiments

Methods:

- <code title="get /api/experiments/health">client.api.experiments.<a href="./src/cortexsdk/resources/api/experiments.py">health_check</a>() -> object</code>

## Public

Methods:

- <code title="get /api/public/room">client.api.public.<a href="./src/cortexsdk/resources/api/public.py">retrieve_room</a>() -> object</code>
- <code title="get /api/public/whoami">client.api.public.<a href="./src/cortexsdk/resources/api/public.py">whoami</a>() -> object</code>

# Healthz

Types:

```python
from cortexsdk.types import HealthzCheckResponse
```

Methods:

- <code title="get /healthz">client.healthz.<a href="./src/cortexsdk/resources/healthz.py">check</a>() -> <a href="./src/cortexsdk/types/healthz_check_response.py">HealthzCheckResponse</a></code>

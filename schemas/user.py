def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "role": item['role']
    }

def usersEntity(items) -> list[dict]:
    return [userEntity(item) for item in items]
from app import user_service

def test_create_user():
    data = {
        "firstName": "John",
        "lastName": "Doe",
        "birthYear": 1990,
        "group": "user"
    }
    user = user_service.create_user(data)
    assert user['firstName'] == "John"
    assert user['lastName'] == "Doe"
    assert user['age'] == 34
    assert user['group'] == "user"

def test_update_user():
    data = {
        "firstName": "John",
        "lastName": "Doe",
        "birthYear": 1990,
        "group": "user"
    }
    user = user_service.create_user(data)

    updated_data = {
        "firstName": "Updated",
        "group": "premium"
    }

    updated_user = user_service.update_user(user['id'], updated_data)
    assert updated_user['firstName'] == "Updated"
    assert updated_user['group'] == "premium"

def test_delete_user():
    data = {
        "firstName": "John",
        "lastName": "Doe",
        "birthYear": 1990,
        "group": "user"
    }
    user = user_service.create_user(data)

    deleted_user = user_service.delete_user(user['id'])
    assert deleted_user == user
    assert len(user_service.get_all_users()) == 0

from api import PetFriends
from settings import user_email, user_password, wrong_password, wrong_email

pf = PetFriends()

# получение ключа с валидным емейл и паролем
def test_get_api_key_for_valid_user(email=user_email, password=user_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result
    print(status)

# получение списка животных с валидным ключом
def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key=pf.get_api_key(user_email,user_password)
    status, result = pf.get_list_of_pets(auth_key,filter)
    assert status == 200
    assert len(result['pets'])>0
    print(status)

#добавление нового питомца с фото
def test_add_pet_with_photo(name='Пес', animal_type='дворняга', age='2', pet_photo='image/image.jpg'):
    _, auth_key =pf.get_api_key(user_email, user_password)
    status, result = pf.add_new_pet_with_photo(auth_key,name,animal_type,age,pet_photo)
    assert status == 200
    assert result['name']==name
    print(status)

#получение ключа при верном вводе емайл и ошибочном пароле
def test_get_api_key_with_correct_mail_and_wrong_password(email=user_email, password =wrong_password):

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result
    print(status)

#получение ключа при вводе ошибочного емайл и верном пароле
def test_get_api_key_with_password_mail_and_wrong_email(email=wrong_email, password = user_password):

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result
    print(status)

#получение ключа при вводе ошибочного емайл и ошибочного пароля
def test_get_api_key_with_password_mail_and_wrong_email(email=wrong_email, password = wrong_password):

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result
    print(status)

#добавление нового животного с незаполненным полем вид животного
def test_add_pet_with_empty_field(name='Пес', animal_type='', age='2'):


    _, api_key = pf.get_api_key(user_email, user_password)
    status, result = pf.add_new_pet_without_photo(api_key, name, animal_type, age)

    assert status == 200

    print('Питомец с незаполненным видом животного добавлен', status)

#добавление нового животного с невалидным именем животного
def test_add_pet_with_valid_data_empty_field(name='1231215129129qweqwrwt', animal_type='кот', age='2'):


    _, api_key = pf.get_api_key(user_email, user_password)
    status, result = pf.add_new_pet_without_photo(api_key, name, animal_type, age)

    assert status == 200

    print('Питомец с невалидным имененем добавлен', status)

#добавление питомца без фото
def test_add_pet_with_without_photo(name='Шарик', animal_type='Пес', age='3'):

    _, api_key = pf.get_api_key(user_email, user_password)
    status, result = pf.add_new_pet_without_photo(api_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    print('Питомец добавлен без фото', status)

#добавление питомца с невалидным возрастом(меньше 0 или больше 20 лет)
def test_add_pet_with_huge_age(name='Аркаша', animal_type='попугай',age='100', pet_photo='image/image.jpg'):

    _, api_key = pf.get_api_key(user_email, user_password)
    status, result = pf.add_new_pet_with_photo(api_key, name, animal_type, age, pet_photo)

    age = float(result['age'])
    assert status == 200
    assert (age > 20 or age < 0), 'Добавлен питомец с невозможным возрастом старше 20 лет.'
    print(f'\n Сайт позволяет добавлять питомеца с невозможным возрастом, меньше 0 или старше 20 лет. {age}')

#добавление питомца с невалидным возрастом(нечисловые значения)
def test_add_pet_with_nonvalid_age(name='Володя', animal_type='Крыса',age='!@?', pet_photo='image/image.jpg'):

    _, api_key = pf.get_api_key(user_email, user_password)
    status, result = pf.add_new_pet_with_photo(api_key, name, animal_type, age, pet_photo)

    assert status == 200

    print(status, 'Добавлен питомец невозможным возрастом', {age})

#удаление первого питомца из списка питомцев
def test_delete_pet():

    _, auth_key = pf.get_api_key(user_email, user_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id not in my_pets.values()

    print(status)
#обновление информации первого питомца из списка питомцев
def test_update_pet_info(name='Лайк', animal_type='пес', age=4):


    _, auth_key = pf.get_api_key(user_email, user_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")


    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 200
        assert result['name'] == name
        print(status)
        print(result)
    else:
        raise Exception("Список питомцев пуст!")


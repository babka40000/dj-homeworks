import pytest as pytest
from rest_framework.test import APIClient
from model_bakery import baker
#
from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_first_course_get(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get('http://127.0.0.1:8000/api/v1/courses/'+str(courses[0].id)+"/")
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == courses[0].id


@pytest.mark.django_db
def test_list_course(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get('http://127.0.0.1:8000/api/v1/courses/')

    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, m in enumerate(data):
        assert m['name'] == courses[i].name


@pytest.mark.django_db
def test_id_filtered(client, course_factory):
    courses = course_factory(_quantity=100)
    response = client.get('http://127.0.0.1:8000/api/v1/courses/?id='+str(courses[0].id))

    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == courses[0].id


@pytest.mark.django_db
def test_name_filtered(client, course_factory):
    courses = course_factory(_quantity=100)
    response = client.get('http://127.0.0.1:8000/api/v1/courses/?name='+str(courses[0].name))

    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == courses[0].name


@pytest.mark.django_db
def test_create_course(client):
    Student.objects.create(id=1, name='Alex')

    data = {'name': 'first', 'students': ['1']}
    res = client.post('http://127.0.0.1:8000/api/v1/courses/', data=data)
    assert res.status_code == 201
    data = res.json()
    print(data)
    assert data['name'] == 'first'


@pytest.mark.django_db
def test_update_course(client, course_factory):
    courses = course_factory(_quantity=10)
    data = {'name': 'test_course'}
    res = client.patch('http://127.0.0.1:8000/api/v1/courses/'+str(courses[5].id)+'/', data=data)

    assert res.status_code == 200
    data = res.json()
    assert data['name'] == 'test_course'


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    courses = course_factory(_quantity=10)
    res = client.delete('http://127.0.0.1:8000/api/v1/courses/' + str(courses[7].id) + '/')
    assert res.status_code == 204

    res = client.get('http://127.0.0.1:8000/api/v1/courses/')
    assert res.status_code == 200

    data = res.json()
    assert len(data) == 9

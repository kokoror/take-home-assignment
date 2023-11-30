from django.test import TestCase
from django.urls import reverse
from .models import TeamMember, Role
from .forms import TeamMemberForm

# To run these test, run command 'python manage.py test' in the console.

#Test Models
class TeamMemberModelTest(TestCase):
    def setUp(self):
        TeamMember.objects.create(
            first_name="Charlene",
            last_name="Pham",
            email="charlene@instawork.com",
            phone="415-310-1619",
            role=Role.REGULAR
        )

    def test_team_member_creation(self):
        member = TeamMember.objects.get(email="charlene@instawork.com")
        self.assertEqual(member.first_name, "Charlene")
        self.assertEqual(member.last_name, "Pham")
        self.assertEqual(member.phone, "415-310-1619")
        self.assertEqual(member.role, Role.REGULAR)

    def test_team_member_string_representation(self):
        member = TeamMember.objects.get(email="charlene@instawork.com")
        self.assertEqual(str(member), "Charlene Pham")


#Test Views
class ViewTestCase(TestCase):

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
    
    def test_update_team_member_view(self):
        member = TeamMember.objects.create(
            first_name="Charlene",
            last_name="Pham",
            email="charlene@instawork.com",
            phone="415-310-1619",
            role=Role.REGULAR
        ) 
        url = reverse('teammember', args=[member.id])

        # Test GET
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test POST
        post_data = {
            'first_name': 'Charlene',
            'last_name': 'Pham',
            'email': 'charlene@instawork.com',
            'phone': '415-310-1619',
            'role': 'Admin'
        }
        response = self.client.post(url, post_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_add_team_member_view(self):
        url = reverse('add_team_member')

        # Test GET
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_team_member.html')

        # Test POST
        post_data = {
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'John@instawork.com',
            'phone': '000-000-0000',
            'role': 'Admin'
        }
        response = self.client.post(url, post_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_delete_team_member_view(self):
        member = TeamMember.objects.create(
            first_name="Charlene",
            last_name="Pham",
            email="charlene@instawork.com",
            phone="415-310-1619",
            role=Role.REGULAR
        ) 
        url = reverse('delete_team_member', args=[member.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertEqual(TeamMember.objects.count(), 0) 
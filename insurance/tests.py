from django.contrib.auth import get_user_model
from django.test import RequestFactory
from .views import InsuranceListView, InsuranceAddView
from django.test import TestCase
from TUBase.models import CustomTUBase
from django.urls import reverse
from django.utils import timezone
from .forms import InsuranceForm
from .models import CustomUser, PolicyStatus, PolicyType, InsurancePolicy


class InsurancePolicyModelTestCase(TestCase):
    def setUp(self):
        self.tu_base = CustomTUBase.objects.create(short_name="TestCompany")
        self.policy_status = PolicyStatus.objects.create(policy_status_name="Active")
        self.policy_type = PolicyType.objects.create(policy_type_name="Car Insurance")
        self.policy_creator = CustomUser.objects.create(username="testuser")

    def test_policy_number_generation(self):
        policy = InsurancePolicy.objects.create(
            tuBase=self.tu_base,
            policy_number="12345678901",
            validity_start_date=timezone.now(),
            validity_end_date=timezone.now(),
            policy_creator=self.policy_creator,
            status=self.policy_status,
            policy_type=self.policy_type,
        )
        expected_policy_number = "TES-12345678901"
        self.assertEqual(policy.policy_number, expected_policy_number)

    def test_policy_string_representation(self):
        policy = InsurancePolicy.objects.create(
            tuBase=self.tu_base,
            policy_number="12345678901",
            validity_start_date=timezone.now(),
            validity_end_date=timezone.now(),
            policy_creator=self.policy_creator,
            status=self.policy_status,
            policy_type=self.policy_type,
        )
        expected_string = "TES-12345678901"
        self.assertEqual(str(policy), expected_string)

    def test_policy_status_string_representation(self):
        policy_status = PolicyStatus.objects.create(policy_status_name="Inactive")
        expected_string = "Inactive"
        self.assertEqual(str(policy_status), expected_string)

    def test_policy_type_string_representation(self):
        policy_type = PolicyType.objects.create(policy_type_name="Home Insurance")
        expected_string = "Home Insurance"
        self.assertEqual(str(policy_type), expected_string)


class UrlsTestCase(TestCase):
    def test_insurance_add_url(self):
        url = reverse("insurance_add")
        self.assertEqual(url, "/insurance_add/")

    def test_insurance_list_url(self):
        url = reverse("insurance_list")
        self.assertEqual(url, "/insurance_list/")

    def test_insurance_edit_url(self):
        url = reverse("insurance_edit", kwargs={"pk": 1})
        self.assertEqual(url, "/insurance_edit/1/")

    def test_insurance_delete_url(self):
        url = reverse("insurance_delete", kwargs={"pk": 1})
        self.assertEqual(url, "/insurance_delete/1/")


class ViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_insurance_list_view(self):
        request = self.factory.get(reverse('insurance_list'))
        request.user = self.user
        response = InsuranceListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_insurance_add_view(self):
        request = self.factory.get(reverse('insurance_add'))
        request.user = self.user
        response = InsuranceAddView.as_view()(request)
        self.assertEqual(response.status_code, 200)


class InsuranceFormTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_missing_required_fields(self):
        form = InsuranceForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('policy_number', form.errors)
        self.assertIn('This field is required.', form.errors['policy_number'])
        self.assertIn('validity_start_date', form.errors)
        self.assertIn('This field is required.', form.errors['validity_start_date'])
        self.assertIn('validity_end_date', form.errors)
        self.assertIn('This field is required.', form.errors['validity_end_date'])
        self.assertIn('status', form.errors)
        self.assertIn('This field is required.', form.errors['status'])
        self.assertIn('policy_type', form.errors)
        self.assertIn('This field is required.', form.errors['policy_type'])

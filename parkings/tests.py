from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Parkings
from .serializers import ParkingsSerializer

# Create your tests here.

class BaseViewTest(APITestCase):
	client = APIClient()

	@staticmethod
	def create_parking(x=0,y=0):
		if not isinstance(x, str) and not isinstance(y, str):
			Parkings.objects.create(x=x,y=y)

	def setUp(self):
		# add test data
		self.create_parking(0, 0)
		self.create_parking(1, 1)
		self.create_parking(2, 2)
		self.create_parking(3, 3)


class GetAllParkingsTest(BaseViewTest):

	def test_get_all_parkings(self):
		# hit the API endpoint
		response = self.client.get(
				reverse("parkings-all")
		)
		# fetch the data from db
		expected = Parkings.objects.all()
		serialized = ParkingsSerializer(expected, many=True)
		self.assertEqual(response.data, serialized.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
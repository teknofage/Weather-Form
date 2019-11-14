from app import app
from unittest import TestCase, main
from unittest.mock import patch, ANY


class AppTests(TestCase): 
    """Run tests on the Weather App."""
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    @patch('app.requests') #decorator
    def test_weather_results(self, requests): #requests refers to fake/mock requests
        #tell requests parameter to equal temp: 60
        requests.get().json.return_value = {
        'main': { 'temp': 300 }
    }
        
        result = self.app.get('/weather_results?city=San+Francisco')
        self.assertEqual(result.status_code, 200)

        page_content = result.get_data(as_text=True)
        self.assertIn("Today's temperature in San Francisco is 80 degrees Fahrenheit", page_content)

        requests.get.assert_called_with(ANY, 
        params={'q': 'San Francisco', 'appid': ANY})
        
        
    @patch('app.requests') #decorator
    def test_weather_results_again(self, requests): #requests refers to fake/mock requests
        #tell requests parameter to equal temp: 60
        requests.get().json.return_value = {
        'main': { 'temp': 300 }
    }
        
        result = self.app.get('/weather_results?city=Jerusalem')
        self.assertEqual(result.status_code, 200)

        page_content = result.get_data(as_text=True)
        self.assertIn("Today's temperature in Jerusalem is 80 degrees Fahrenheit", page_content)

        requests.get.assert_called_with(ANY, 
        params={'q': 'Jerusalem', 'appid': ANY})

if __name__ == '__main__':
    main()
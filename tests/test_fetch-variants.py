import pytest
from flask import Flask
from flask_testing import TestCase
from ensembl_variant_lookup import app

class TestEnsemblVariantLookup(TestCase):
    def create_app(self):
        app = app()
        app.config['TESTING'] = True
        return app

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('index.html')

    def test_single_variant_lookup_page(self):
        response = self.client.get('/variant')
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('variant_results.html')

    def test_batch_variant_lookup_page(self):
        response = self.client.get('/batch')
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('batch_results.html')

    def test_gene_lookup_page(self):
        response = self.client.get('/visualize')
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('region_results.html')

    def test_single_variant_lookup(self):
        response = self.client.post('/variant', data={'rsid': 'rs201937405'})
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('variant_results.html')

    def test_batch_variant_lookup(self):
        response = self.client.post('/batch', data={'rsid_list': 'rs201937405,rs123456'})
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('batch_results.html')

    def test_gene_lookup(self):
        response = self.client.post('/visualize', data={'gene_name': 'BRCA1'})
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('region_results.html')

if __name__ == '__main__':
    pytest.main()

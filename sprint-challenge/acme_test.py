#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_flammability(self):
        """Test default product flammability being 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_stealability(self):
        """Test high price and low weight => high stealability."""
        prod = Product('Test Product', price=100, weight=1)
        self.assertEqual(prod.stealability(), "Very stealable!")

    def test_explode(self):
        """Test highish flamability + mid weight => \"...boom!\" """
        prod = Product('Test Product', weight=4, flammability=10)
        self.assertEqual(prod.explode(), "...boom!")


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme product *reports* are the tops!"""
    def test_default_num_products(self):
        """Test that 30 products are generated by default."""
        gen_prods = generate_products()
        self.assertEqual(len(gen_prods), 30)

    def test_legal_names(self):
        """Check that all generated names are valid by making sure
           first part of a name is in ADJECTIVES and second part
           is in NOUNS."""
        gen_prods_split = [p.name.split(" ")
                           for p in generate_products()]
        should_be_adjs = [n[0] for n in gen_prods_split]
        should_be_nouns = [n[1] for n in gen_prods_split]

        for a in should_be_adjs:
            self.assertIn(a, ADJECTIVES)

        for n in should_be_nouns:
            self.assertIn(n, NOUNS)

if __name__ == '__main__':
    unittest.main()
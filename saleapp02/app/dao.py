def load_categories():
    return [{
        'id': 1,
        'name': 'Điện thoại'
    },
        {
            'id': 2,
            'name': 'Ipad'
        },
        {
            'id': 3,
            'name': 'Macbook'
        },
        {
            'id': 4,
            'name': 'Apple Watch'
        },
        {
            'id': 5,
            'name': 'Phụ kiện Apple'
        }]


def load_products(kw=None):
    products = [{
        'id': 1,
        'name': "Iphone 15 128GB",
        'price': '20.990.000',
        'image': 'https://cdn1.viettelstore.vn/Images/Product/ProductImage/1979390149.jpeg'
    }, {
        'id': 2,
        'name': "Iphone 15 Pro 128GB",
        'price': '27.990.000',
        'image': 'https://cdn.viettelstore.vn/Images/Product/ProductImage/1778159139.jpeg'
    }, {
        'id': 3,
        'name': "Iphone 15 Pro Max 256GB",
        'price': '27.990.000',
        'image': 'https://cdn1.viettelstore.vn/Images/Product/ProductImage/1349547788.jpeg'
    }, {
        'id': 4,
        'name': "Iphone 15 Plus 128GB",
        'price': '27.990.000',
        'image': 'https://cdn1.viettelstore.vn/Images/Product/ProductImage/1877671236.jpeg'
    }, {
        'id': 5,
        'name': "IPad Pro 11 (2022) WIFI 128GB",
        'price': '20.090.000',
        'image': 'https://cdn1.viettelstore.vn/Images/Product/ProductImage/1668025194.jpeg'
    }, {
        'id': 6,
        'name': "IPad Gen 10 WIFI 64GB",
        'price': '10.890.000',
        'image': 'https://cdn1.viettelstore.vn/Images/Product/ProductImage/2145259476.jpeg'
    }, {
        'id': 7,
        'name': "Apple Watch Series 8 viền thép dây Milanese Cellular 41mm",
        'price': '18.690.000',
        'image': 'https://cdn1.viettelstore.vn/Images/Product/ProductImage/1806036517.jpeg'
    }, {
        'id': 8,
        'name': "Apple Watch SE (2022) Cellular 40mm",
        'price': '7.190.000',
        'image': 'https://cdn1.viettelstore.vn/Images/Product/ProductImage/1748330060.jpeg'
    }, {
        'id': 9,
        'name': "Apple Watch Ultra viền Titanium dây Ocean Band 49mm",
        'price': '18.690.000',
        'image': 'https://cdn1.viettelstore.vn/Images/Product/ProductImage/1751803236.jpeg'
    }, {
        'id': 10,
        'name': "Laptop Apple MacBook Air 13 inch M1 2020 8-core CPU/8GB/256GB/7-core GPU (MGN63SA/A)",
        'price': '19.690.000',
        'image': 'https://cdn.tgdd.vn/Products/Images/44/231244/macbook-air-m1-2020-silver-01-org.jpg'
    }, {
        'id': 11,
        'name': "Laptop MacBook Pro 16 inch M2 Pro 2023 12-core CPU/16GB/1TB/19-core GPU (MNWD3SA/A)",
        'price': '65.990.000',
        'image': 'https://cdn.tgdd.vn/Products/Images/44/302150/macbook-pro-16-inch-m2-pro-1tb-silver-abc-1.jpg'
    }, {
        'id': 12,
        'name': "Laptop Apple MacBook Air 13 inch M2 2022 8-core CPU/16GB/512GB/10-core GPU (Z15Z0003L)",
        'price': '39.190.000',
        'image': 'https://cdn.tgdd.vn/Products/Images/44/289441/apple-macbook-air-m2-2022-16gb-1-1.jpg'
    }]


    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    return products
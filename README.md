# ASD Group Project Backend
Backend for the ASD Group Project

# MongoDB details
### Database name: HRMS
## Collection export files (JSON):
Can be imported easily using <b>MongoDB Compass</b>

### Staff
[{
  "_id": {
    "$oid": "659afc824dd2d0b781b7ec57"
  },
  "staffId": 1,
  "password": {
    "$binary": {
      "base64": "JDJiJDEyJGVINFFWZFhFWmZGWElwUGdidXZnWC4xbmhGNDFlOENRZEpPVnVLeXY2c2lMUmVLSy9SOC8u",
      "subType": "00"
    }
  },
  "role": "Chef",
  "name": "John",
  "shift": "9-15",
  "metrics": 0
},
{
  "_id": {
    "$oid": "659afd554dd2d0b781b7ec5a"
  },
  "staffId": 2,
  "password": {
    "$binary": {
      "base64": "JDJiJDEyJFdNZmNUOFZpY1pweTZFZG43YjRhVC5PMW1PUldnMUV3aGJPbDluZ1hLR2VBUVN6SDZrLmth",
      "subType": "00"
    }
  },
  "role": "Waitstaff",
  "name": "Jane",
  "shift": "9-15",
  "metrics": 0
}]
### Orders
[{
  "_id": {
    "$oid": "659b1bbe5da30d56794a09cf"
  },
  "orderId": 1,
  "items": [
    {
      "itemId": 1,
      "name": "Chicken Breast",
      "price": "8.50£",
      "availability": "True",
      "itemType": "Food",
      "description": "Pan-fried chicken breast with a side of rice"
    },
    {
      "itemId": 2,
      "name": "Coca-Cola",
      "price": "1.80£",
      "availability": "True",
      "itemType": "Drink",
      "description": ""
    },
    {
      "itemId": 3,
      "name": "Mango",
      "price": "2£",
      "availability": "True",
      "itemType": "Dessert",
      "description": "Sliced Mango"
    }
  ]
},
{
  "_id": {
    "$oid": "659b1bce5da30d56794a09d0"
  },
  "orderId": 2,
  "items": [
    {
      "itemId": 1,
      "name": "Chicken Breast",
      "price": "8.50£",
      "availability": "True",
      "itemType": "Food",
      "description": "Pan-fried chicken breast with a side of rice"
    },
    {
      "itemId": 2,
      "name": "Coca-Cola",
      "price": "1.80£",
      "availability": "True",
      "itemType": "Drink",
      "description": ""
    },
    {
      "itemId": 3,
      "name": "Mango",
      "price": "2£",
      "availability": "True",
      "itemType": "Dessert",
      "description": "Sliced Mango"
    }
  ]
},
{
  "_id": {
    "$oid": "659b1bcf5da30d56794a09d1"
  },
  "orderId": 3,
  "items": [
    {
      "itemId": 1,
      "name": "Chicken Breast",
      "price": "8.50£",
      "availability": "True",
      "itemType": "Food",
      "description": "Pan-fried chicken breast with a side of rice"
    },
    {
      "itemId": 2,
      "name": "Coca-Cola",
      "price": "1.80£",
      "availability": "True",
      "itemType": "Drink",
      "description": ""
    },
    {
      "itemId": 3,
      "name": "Mango",
      "price": "2£",
      "availability": "True",
      "itemType": "Dessert",
      "description": "Sliced Mango"
    }
  ]
}]
### Menus
[{
  "_id": {
    "$oid": "659b09f9496bd38d3b22baee"
  },
  "menuId": 1,
  "active": "True",
  "items": [
    {
      "itemId": 1,
      "name": "Chicken Breast",
      "price": "8.50£",
      "availability": "True",
      "itemType": "Food",
      "description": "Pan-fried chicken breast with a side of rice"
    },
    {
      "itemId": 2,
      "name": "Coca-Cola",
      "price": "1.80£",
      "availability": "True",
      "itemType": "Drink",
      "description": ""
    },
    {
      "itemId": 3,
      "name": "Mango",
      "price": "2£",
      "availability": "True",
      "itemType": "Dessert",
      "description": "Sliced Mango"
    }
  ]
}]
### Menu Items
[{
  "_id": {
    "$oid": "659b0c40468fca3c0aa25be6"
  },
  "itemId": 3,
  "name": "Mango",
  "price": "2£",
  "description": "Sliced Mango",
  "itemType": null,
  "availability": "True"
},
{
  "_id": {
    "$oid": "659b0c5b1be27ceefadcf15d"
  },
  "itemId": 2,
  "name": "Coca-Cola",
  "price": "1.80£",
  "description": "",
  "itemType": null,
  "availability": "True"
},
{
  "_id": {
    "$oid": "659b0bbad62cb3cea887c387"
  },
  "itemId": 1,
  "name": "Chicken Breast",
  "price": "8.50£",
  "description": "Pan-fried chicken breast with a side of rice",
  "itemType": null,
  "availability": "True"
}]
### Inventory Items
[{
  "_id": {
    "$oid": "659727e87bd6d93f0a5f7b87"
  },
  "itemId": 1,
  "name": "Potato",
  "price": "10p",
  "amount": 100
}]


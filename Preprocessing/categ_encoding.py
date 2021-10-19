def encode(data):

    country_map = {'Other': 80,'South Africa': 1406,'Nigeria': 1194,"Côte d'Ivoire": 1083,'Uganda': 779,'Vietnam': 688,'Zambia': 683,'Haiti': 655,'Mozambique': 631,'Zimbabwe': 538,'Tanzania': 155}
    data.Coutry=data.Coutry.map(country_map)

    data['Manufacturing Site'] = data['Manufacturing Site'].map(manuf_site_map)

    data.Brand = data.Brand.map(brand_map)

    data['Item Description'] = data['Item Description'].map(item_map)

    data['Product Group'] = data['Product Group'].map(prod_group_map)

    data['Sub Classification'] = data['Sub Classification'].map(sub_class_map)

    data['Molecule/Test Type'] = data['Molecule/Test Type'].map(test_type_map)

    data['Dosage Form'] = data['Dosage Form'].map(dosage_form_map)

    data.Dosage = data.Dosage.map(dosage_map)

    data['Managed By'] = data['Managed By'].map(managed_by_map)

    data['Shipment Mode'] = data['Shipment Mode'].map(shipment_mode_map)

    data['Freight_cost_special'] = data['Freight_cost_special'].map(freight_spcl_map)

    return data

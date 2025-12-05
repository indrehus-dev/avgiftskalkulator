import math

def calc_from_gross(gross):
    if gross is None:
        return None, None
    fee = min(max(0.10 * gross, 25), 55)
    net = gross - fee
    return fee, net

def calc_from_net(net):
    if net is None:
        return None, None
    
    if net < 225:
        gross = net + 25
    elif net <= 495:
        gross = net / 0.9
    else:
        gross = net + 55
        
    fee = gross - net
    return fee, gross

def test_logic():
    # Test cases from HTML comments/examples
    
    # Gross tests
    # 200 -> 25 kr fee
    f, n = calc_from_gross(200)
    print(f"Gross 200: Fee={f} (Exp: 25)")
    assert f == 25
    
    # 500 -> 50 kr fee
    f, n = calc_from_gross(500)
    print(f"Gross 500: Fee={f} (Exp: 50)")
    assert f == 50
    
    # 600 -> 55 kr fee
    f, n = calc_from_gross(600)
    print(f"Gross 600: Fee={f} (Exp: 55)")
    assert f == 55

    # Net tests
    # < 225 -> +25
    # 175 -> +25 = 200 gross, fee 25
    f, g = calc_from_net(175)
    print(f"Net 175: Gross={g} (Exp: 200), Fee={f} (Exp: 25)")
    assert g == 200
    assert f == 25
    
    # 225-495 -> / 0.9
    # 450 -> 450 / 0.9 = 500 gross, fee 50
    f, g = calc_from_net(450)
    print(f"Net 450: Gross={g} (Exp: 500), Fee={f} (Exp: 50)")
    assert abs(g - 500) < 0.001
    assert abs(f - 50) < 0.001
    
    # > 495 -> +55
    # 545 -> +55 = 600 gross, fee 55
    f, g = calc_from_net(545)
    print(f"Net 545: Gross={g} (Exp: 600), Fee={f} (Exp: 55)")
    assert g == 600
    assert f == 55

    print("All tests passed!")

if __name__ == "__main__":
    test_logic()

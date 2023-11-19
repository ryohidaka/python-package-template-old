from python_package_template.python_package_template import PythonPackageTemplate


def test_initial_counter_value():
    template_instance = PythonPackageTemplate()
    assert template_instance.counter == 0


def test_add_numbers():
    template_instance = PythonPackageTemplate()
    result = template_instance.add_numbers(3, 5)
    assert result == 8
    assert template_instance.counter == 1


def test_add_numbers_negative_values():
    template_instance = PythonPackageTemplate()
    result = template_instance.add_numbers(-2, 7)
    assert result == 5
    assert template_instance.counter == 1

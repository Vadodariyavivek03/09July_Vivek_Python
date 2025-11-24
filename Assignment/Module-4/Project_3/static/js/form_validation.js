function validateForm() {
    let name = document.getElementById('name').value;
    let age = document.getElementById('age').value;
    let email = document.getElementById('email').value;
    let phone = document.getElementById('phone').value;


    if (name === '') {
        alert('Name is required');
        return false;
    }
    if (age === '' || age <= 0) {
        alert('Enter a valid age');
        return false;
    }
    if (email === '') {
        alert('Email is required');
        return false;
    }
    let phonePattern = /^\d{10}$/;
    if (!phonePattern.test(phone)) {
        alert('Enter a valid 10-digit phone number');
        return false;
    }
    return true;
}
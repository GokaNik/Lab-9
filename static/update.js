function addContact() {
    let contactName = document.getElementById('name').value; // Исправлено с 'prod_name' на 'name'
    let phone = document.getElementById('phone').value;

    fetch('/add', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'name': contactName, 'phone': phone}) // Убраны ненужные поля
    })
    .then(response => response.json())
    .then(data => {
        if (data.contact) {
            let contactList = document.getElementById("contactsList");
            let li = document.createElement("li");
            li.textContent = `${data.contact.name} - ${data.contact.phone}`;
            contactList.appendChild(li);
        } else {
            alert("Ошибка при добавлении контакта!");
        }
    })
    .catch(error => console.error("Ошибка:", error));
}

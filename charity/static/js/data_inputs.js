document.addEventListener("DOMContentLoaded", function () {

    // Step 1
    let categories = document.getElementsByName('categories');
    let categories_values = []
    categories.forEach((checkbox) => {
        checkbox.addEventListener('change', (event) => {
            if (event.target.checked) {
                categories_values.push(event.target.id)
            }
        })
    })

    // Step 2
    let bags = document.querySelector("input[name='bags']");

    // Step 3
    let orgs = document.querySelectorAll("input[name='organization']");

    function showOrg() {
        if (this.checked) {
            summary_organisation.innerText = `Dla ` + this.id;
        }
    }

    for (let org of orgs) {
        org.addEventListener('change', showOrg);
    }

    // Step 4
    // Mailing data
    let address = document.querySelector("input[name='address']");
    let city = document.querySelector("input[name='city']");
    let postcode = document.querySelector("input[name='postcode']");
    let phone = document.querySelector("input[name='phone']");
    let data = document.querySelector("input[name='data']");
    let time = document.querySelector("input[name='time']");
    let more_info = document.querySelector("textarea[name='more_info']");

    // Step 5
    // Summary - main info
    let summary_bags_categories = document.getElementById("summary_bags_categories");
    bags.addEventListener("change", () => {
        return summary_bags_categories.innerText = bags.value + " sztuk worków zawierających " + categories_values.join(', ');
    });

    let summary_organisation = document.getElementById("summary_organisation");


    // Summary - left side
    let address_output = document.getElementById("address");
    address.addEventListener("change", () => {
        return address_output.innerText = `${address.value}`;
    });

    let city_output = document.getElementById("city");
    city.addEventListener("change", () => {
        return city_output.innerText = city.value;
    });

    let postcode_output = document.getElementById("zipcode");
    postcode.addEventListener("change", () => {
        return postcode_output.innerText = postcode.value;
    });

    let phone_output = document.getElementById("phonenumber");
    phone.addEventListener("change", () => {
        return phone_output.innerText = phone.value;
    });

    // Summary - right side
    let data_output = document.getElementById("pickup_date");
    data.addEventListener("change", () => {
        return data_output.innerText = data.value;
    });

    let time_output = document.getElementById("pickup_time");
    time.addEventListener("change", () => {
        return time_output.innerText = time.value;
    });

    let more_info_output = document.getElementById("pickup_info");
    more_info.addEventListener("change", () => {
        return more_info_output.innerText = more_info.value;
    });
});
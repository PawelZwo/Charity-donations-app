document.addEventListener("DOMContentLoaded", function () {

    // Step 1
    const categories = document.getElementsByName('categories');
    let categories_values = []
    categories.forEach((checkbox) => {
        checkbox.addEventListener('change', (event) => {
            if (event.target.checked) {
                categories_values.push(event.target.value)
            }
        })
    })

    // Step 2
    const bags = document.querySelector("input[name='bags']");

    // Step 3
    const orgs = document.querySelectorAll("input[name='organization']");

    function showOrg() {
        if (this.checked) {
            summary_organisation.innerText = `Dla ` + this.value;
        }
    }

    for (const org of orgs) {
        org.addEventListener('change', showOrg);
    }

    // Step 4
    // Mailing data
    const address = document.querySelector("input[name='address']");
    const city = document.querySelector("input[name='city']");
    const postcode = document.querySelector("input[name='postcode']");
    const phone = document.querySelector("input[name='phone']");
    const data = document.querySelector("input[name='data']");
    const time = document.querySelector("input[name='time']");
    const more_info = document.querySelector("textarea[name='more_info']");

    // Step 5
    // Summary - main info
    const summary_bags_categories = document.getElementById("summary_bags_categories");
    bags.addEventListener("change", () => {
        return summary_bags_categories.innerText = bags.value + " sztuk worków zawierających " + categories_values.join(', ');
    });

    const summary_organisation = document.getElementById("summary_organisation");


    // Summary - left side
    const address_output = document.getElementById("address");
    address.addEventListener("change", () => {
        return address_output.innerText = `${address.value}`;
    });

    const city_output = document.getElementById("city");
    city.addEventListener("change", () => {
        return city_output.innerText = city.value;
    });

    const postcode_output = document.getElementById("zipcode");
    postcode.addEventListener("change", () => {
        return postcode_output.innerText = postcode.value;
    });

    const phone_output = document.getElementById("phonenumber");
    phone.addEventListener("change", () => {
        return phone_output.innerText = phone.value;
    });

    // Summary - right side
    const data_output = document.getElementById("pickup_date");
    data.addEventListener("change", () => {
        return data_output.innerText = data.value;
    });

    const time_output = document.getElementById("pickup_time");
    time.addEventListener("change", () => {
        return time_output.innerText = time.value;
    });

    const more_info_output = document.getElementById("pickup_info");
    more_info.addEventListener("change", () => {
        return more_info_output.innerText = more_info.value;
    });
});
const portfolioFlexContainer = document.querySelector('.portfolio-flex');
const entryFlexContainer = document.querySelector('.entry-flex');

function changeBox(value1) {
    portfolioFlexContainer.style.display = 'none';
    entryFlexContainer.style.display = 'flex';
    let valueEntryInformation = document.getElementById(value1);
    valueEntryInformation.style.display = 'flex';
}

function closeOut() {
    portfolioFlexContainer.style.display = 'flex';
    entryFlexContainer.style.display = 'none';
    let valueInfo = document.querySelectorAll(".value-information");
    if (entryFlexContainer.style.display === 'none') {
        valueInfo.forEach((element) => {
            element.style.display = 'none';
        })
    } else {
        valueInfo.forEach((element) => {
            element.style.display = 'flex';
        })
    }
}
const searchInput = document.getElementById("search-input");
const speciesFilter = document.getElementById("species-filter");
const animalCards = Array.from(document.querySelectorAll(".animal-card"));
const visibleCount = document.getElementById("visible-count");
const noResults = document.getElementById("no-results");

const toast = document.getElementById("toast");
const modal = document.getElementById("proposal-modal");
const modalEmoji = document.getElementById("modal-emoji");
const modalTitle = document.getElementById("modal-title");
const modalMessage = document.getElementById("modal-message");
const compatibilityScore = document.getElementById("compatibility-score");
const scoreBar = document.getElementById("score-bar");
const modalVerdict = document.getElementById("modal-verdict");

const closeModalButton = document.getElementById("close-modal");
const doneButton = document.getElementById("modal-done");
const randomMatchButton = document.getElementById("random-match");

let toastTimer;
let lastFocusedElement = null;


function showToast(message) {
    toast.textContent = message;
    toast.classList.add("show");

    clearTimeout(toastTimer);

    toastTimer = setTimeout(() => {
        toast.classList.remove("show");
    }, 2800);
}


function filterAnimals() {
    const query = searchInput.value.trim().toLowerCase();
    const selectedSpecies = speciesFilter.value;

    let count = 0;

    animalCards.forEach((card) => {
        const name = card.dataset.name || "";
        const breed = card.dataset.breed || "";
        const species = card.dataset.species || "";

        const matchesSearch =
            name.includes(query) || breed.includes(query);

        const matchesSpecies =
            selectedSpecies === "All" || species === selectedSpecies;

        const visible = matchesSearch && matchesSpecies;

        card.hidden = !visible;

        if (visible) {
            count++;
        }
    });

    visibleCount.textContent = count;
    noResults.hidden = count !== 0;
}


searchInput.addEventListener("input", filterAnimals);
speciesFilter.addEventListener("change", filterAnimals);


const funnyVerdicts = [
    "The stars approve. The grass committee needs to investigate.",
    "Your families have started planning the wedding without asking you.",
    "This relationship has more red flags than a goat festival.",
    "One of you wants love. The other wants unlimited snacks.",
    "The astrologer has resigned after seeing your biodatas.",
    "Your future together is uncertain. Your appetite is not.",
    "The wedding budget has been spent entirely on grass.",
    "Your love story is being sponsored by absolutely nobody."
];


const rejectionMessages = [
    "Rishta rejected. Even the grass is disappointed. 🥲",
    "Rejection successful. Your bakra has left the chat. 🐐",
    "Ouch! A whole family of goats just unfollowed you. 💀",
    "Rishta declined. Please touch some grass. 🌱",
    "Breaking news: Another animal chooses drama over love. 😂"
];


function openModal() {
    lastFocusedElement = document.activeElement;

    modal.hidden = false;
    document.body.style.overflow = "hidden";

    closeModalButton.focus();
}


function closeModal() {
    modal.hidden = true;
    document.body.style.overflow = "";

    if (lastFocusedElement) {
        lastFocusedElement.focus();
    }
}


function sendProposal(name, species) {
    const score = Math.floor(Math.random() * 101);
    const verdict =
        funnyVerdicts[Math.floor(Math.random() * funnyVerdicts.length)];

    modalEmoji.textContent = score >= 70 ? "💘" : score >= 40 ? "💍" : "💀";

    modalTitle.textContent = `Rishta Report: ${name}`;

    modalMessage.textContent =
        `Your proposal has been sent to ${name}, the ${species}. ` +
        "The fictional animal matrimonial committee has reviewed your case.";

    compatibilityScore.textContent = `${score}%`;
    scoreBar.style.width = "0%";

    modalVerdict.textContent = verdict;

    openModal();

    requestAnimationFrame(() => {
        scoreBar.style.width = `${score}%`;
    });
}


document.querySelectorAll(".proposal-btn").forEach((button) => {
    button.addEventListener("click", () => {
        sendProposal(button.dataset.name, button.dataset.species);
    });
});


document.querySelectorAll(".reject-btn").forEach((button) => {
    button.addEventListener("click", () => {
        const message =
            rejectionMessages[
                Math.floor(Math.random() * rejectionMessages.length)
            ];

        showToast(`${button.dataset.name}: ${message}`);
    });
});


randomMatchButton.addEventListener("click", () => {
    const availableCards = animalCards.filter((card) => !card.hidden);

    if (availableCards.length === 0) {
        showToast("No bakras found! Change your search first. 🥲");
        return;
    }

    const randomCard =
        availableCards[Math.floor(Math.random() * availableCards.length)];

    const name = randomCard.querySelector("h3").childNodes[0].textContent.trim();
    const species = randomCard.dataset.species;

    sendProposal(name, species);
});


closeModalButton.addEventListener("click", closeModal);
doneButton.addEventListener("click", closeModal);


modal.addEventListener("click", (event) => {
    if (event.target === modal) {
        closeModal();
    }
});


document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && !modal.hidden) {
        closeModal();
    }
});


filterAnimals();

let score = 0;

document.querySelector('.coin').addEventListener('click', () => {
    score++;
    alert(`Твои очки: ${score}`);
});

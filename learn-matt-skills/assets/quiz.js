/* ============================================================
   Reusable quiz widget — retrieval-practice feedback loop.
   Markup:
   <div class="quiz" data-answer="1">
     <p class="q">Question?</p>
     <button>Option A</button>
     <button>Option B</button>
     <button>Option C</button>
     <p class="explain" hidden>Why the answer is what it is.</p>
   </div>
   data-answer is the 0-based index of the correct button.
   Per the teach skill: answers should be equal length, no
   formatting tells. This file just runs the feedback loop.
   ============================================================ */
document.querySelectorAll(".quiz").forEach((quiz) => {
  const correct = Number(quiz.dataset.answer);
  const buttons = [...quiz.querySelectorAll("button")];
  const explain = quiz.querySelector(".explain");
  buttons.forEach((btn, i) => {
    btn.addEventListener("click", () => {
      buttons.forEach((b) => (b.disabled = true));
      buttons[correct].classList.add("right");
      if (i !== correct) btn.classList.add("wrong");
      if (explain) explain.hidden = false;
    });
  });
});

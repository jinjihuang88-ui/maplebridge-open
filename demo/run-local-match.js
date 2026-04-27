const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const dataFile = path.join(root, "examples", "sample-payloads.json");

function overlapScore(left, right, weight) {
  if (!left?.length || !right?.length) return 0;
  const rightSet = new Set(right.map((item) => item.toLowerCase()));
  const matches = left.filter((item) => rightSet.has(item.toLowerCase())).length;
  return weight * (matches / Math.max(left.length, 1));
}

function scoreMatch(buyer, supplier) {
  let score = 0;
  const reasons = [];

  if (buyer.product_category.toLowerCase() === supplier.product_category.toLowerCase()) {
    score += 0.3;
    reasons.push("category fit");
  }

  const buyerMoq = buyer.moq?.value;
  const supplierMoq = supplier.moq?.value;
  if (supplierMoq && buyerMoq && supplierMoq <= buyerMoq) {
    score += 0.2;
    reasons.push("MOQ fit");
  }

  const compliance = overlapScore(buyer.compliance, supplier.compliance, 0.17);
  if (compliance > 0) {
    score += compliance;
    reasons.push("compliance fit");
  }

  const channels = (supplier.channels || []).join(" ").toLowerCase();
  if (channels.includes("north america") || channels.includes(buyer.country.toLowerCase())) {
    score += 0.15;
    reasons.push("North America export fit");
  }

  score += Math.min(Number(supplier.confidence || 0) * 0.1, 0.1);
  return { score: Number(score.toFixed(2)), reasons };
}

const data = JSON.parse(fs.readFileSync(dataFile, "utf8"));
const buyer = data.buyer_intents[0];

const ranked = data.supplier_intents
  .map((supplier) => ({ supplier, ...scoreMatch(buyer, supplier) }))
  .sort((a, b) => b.score - a.score);

const best = ranked[0];

console.log(`Buyer intent: ${buyer.summary}`);
console.log(`Best supplier: ${best.supplier.summary}`);
console.log(`Match score: ${best.score}`);
console.log(`Why it matched: ${best.reasons.join(", ")}`);
console.log("Review state: human_review_recommended");

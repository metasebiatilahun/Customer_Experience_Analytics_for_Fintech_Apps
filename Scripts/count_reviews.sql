SELECT b.bank_name, COUNT(r.review_id) AS total_reviews
FROM banks_info b
LEFT JOIN reviews r ON b.bank_id = r.bank_id
GROUP BY b.bank_name;
SELECT b.bank_name, COUNT(*) as review_count
FROM banks_info b
GROUP BY b.bank_name;
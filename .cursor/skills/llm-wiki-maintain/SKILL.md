---
name: llm-wiki-maintain
description: >-
  Audit dan perawatan wiki riset — indeks, tautan, registri sumber, job
  partial, status tinjauan. Gunakan saat pengguna meminta audit wiki, perbaiki
  tautan/indeks, atau cek konsistensi state dan wiki.
disable-model-invocation: true
---

# LLM Wiki — maintain

## Alur

1. Rules core + baca `AGENTS.md` → `rules/schema.md` → `skills/maintain.md`
2. Tentukan mode: audit | audit hanya-baca | perbaikan (izin AGENTS.md)
3. Ikuti pemeriksaan dan perbaikan di `skills/maintain.md`

## Contoh prompt

«Audit wiki hanya-baca — fokus job partial dan duplikasi sumber»

«Perbaiki indeks/tautan yang targetnya pasti; usulkan perubahan substantif terpisah»

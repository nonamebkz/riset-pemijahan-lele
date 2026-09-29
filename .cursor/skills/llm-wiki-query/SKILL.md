---
name: llm-wiki-query
description: >-
  Menjawab pertanyaan dari wiki riset dengan bukti terlacak ke raw/ dan
  halaman sumber/konsep. Gunakan saat pengguna bertanya tentang isi wiki,
  pemijahan lele berdasarkan koleksi, atau meminta jawaban hanya-baca dari wiki.
disable-model-invocation: true
---

# LLM Wiki — query

## Alur

1. Rules core + baca `AGENTS.md` → `rules/schema.md` → `skills/query.md`
2. Ikuti alur di `skills/query.md`
3. Perbaikan struktural/bukti → arahkan ke skill `llm-wiki-maintain`

## Contoh prompt

«Jawab dari wiki: … (hanya-baca)»

«Baca pedoman dan skills/query.md. Jawab berdasarkan wiki dengan rujukan.»

import json

from src.synonyms import SEED_SYNONYMS, _full_table, expand_with_synonyms


def test_drug_brand_to_generic():
    out = expand_with_synonyms("give Lasix 40 mg IV")
    assert "furosemide" in out.lower()


def test_abbreviation_expansion_to_long_form():
    out = expand_with_synonyms("afib with RVR")
    low = out.lower()
    assert "atrial fibrillation" in low
    assert "rapid ventricular response" in low


def test_anesthesia_abbrevs():
    out = expand_with_synonyms("LAST treatment")
    assert "local anesthetic systemic toxicity" in out.lower()


def test_mac_abbrev():
    out = expand_with_synonyms("MAC of sevoflurane")
    assert "minimum alveolar concentration" in out.lower()


def test_unknown_terms_pass_through():
    q = "unrelated random query foo bar"
    assert expand_with_synonyms(q) == q


def test_seed_table_has_high_yield_entries():
    table = _full_table()
    for must in ["afib", "mi", "copd", "lasix", "ativan", "last", "mh", "ekg", "abg", "cico"]:
        assert must in table, f"seed table missing {must}"


def test_extra_synonyms_loaded(tmp_path, monkeypatch):
    from src import synonyms

    extra = tmp_path / "synonyms_extra.json"
    extra.write_text(json.dumps({"booboo": "boo-boo unique-marker"}), encoding="utf-8")
    monkeypatch.setattr(synonyms.settings, "data_dir", tmp_path)
    synonyms._full_table.cache_clear()
    out = synonyms.expand_with_synonyms("booboo")
    assert "unique-marker" in out


def test_does_not_double_apply_same_phrase():
    out = expand_with_synonyms("MAC value of sevoflurane MAC")
    assert out.lower().count("minimum alveolar concentration") == 1

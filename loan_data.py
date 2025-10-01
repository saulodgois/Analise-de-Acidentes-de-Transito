from pathlib import Path
import pandas as pd
import csv

def load_and_prepare_data(filename: str, data_dir: str = "data"):

    base = Path(__file__).parent
    filepath = (base / data_dir / filename).resolve()
    print(f"[i] Procurando arquivo em: {filepath}")

    if not filepath.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")

    size_mb = filepath.stat().st_size / (1024 * 1024)
    print(f"[i] Tamanho do arquivo: {size_mb:.2f} MB")

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        sample_lines = [next(f) for _ in range(10)]
    sample = "".join(sample_lines)

    try:
        dialect = csv.Sniffer().sniff(sample)
        sep = dialect.delimiter
    except Exception:
        sep = ","

    print(f"[i] Delimiter detectado (tentativa): {repr(sep)}")

    read_kwargs = {
        "filepath_or_buffer": str(filepath),
        "sep": sep,
        "low_memory": False
    }

    header_cols = sample.splitlines()[0].split(sep)
    header_cols = [c.strip().strip('"').strip("'") for c in header_cols]
    if "Start_Time" in header_cols:
        read_kwargs["parse_dates"] = ["Start_Time"]

    df = None
    for enc in ("utf-8-sig", "utf-8", "latin1"):
        try:
            print(f"[i] Tentando ler com encoding={enc} ...")
            df = pd.read_csv(**read_kwargs, encoding=enc)
            print(f"[OK] Leitura bem-sucedida com encoding={enc}")
            break
        except Exception as e:
            print(f"[!] Falhou com encoding={enc}: {e}")

    if df is None:

        try:
            print("[i] Tentativa final com engine='python' e sep=',' ...")
            df = pd.read_csv(str(filepath), engine="python")
            print("[OK] Leitura com engine='python' bem-sucedida")
        except Exception as e:
            raise RuntimeError(f"Falha ao ler CSV: {e}")

    print(f"[i] Colunas encontradas ({len(df.columns)}): {df.columns.tolist()[:20]}")
    print(f"[i] Shape: {df.shape}")

    # Converter Start_Time para datetime se ainda não estiver
    df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors="coerce")
    
    # Extrair dia da semana (0 = Segunda, 6 = Domingo)
    df['Day_of_Week'] = df['Start_Time'].dt.strftime('%A')
    
    # Extrair hora do dia
    df['Hour'] = df['Start_Time'].dt.hour
    
    if "Start_Time" in df.columns:
        n_na = df["Start_Time"].isna().sum()
        print(f"[i] Start_Time convertido -> {n_na} valores inválidos (serão removidos)")
        df = df.dropna(subset=["Start_Time"]).reset_index(drop=True)
    else:
        print("[aviso] Coluna 'Start_Time' não encontrada no arquivo. Continue conforme necessário.")

    return df

#!/usr/bin/env bash
set -euo pipefail
# Usage: VM=ubuntu@<vm-ip> ./deploy/migrate_to_vm.sh
: "${VM:?set VM=ubuntu@<ip>}"
DEST=/home/ubuntu/anesthesia_attending
# -L dereferences the storage/chroma junction (-> D:) so the real index is copied
rsync -avzL --progress storage/chroma/ "$VM:$DEST/storage/chroma/"
rsync -avz storage/sqlite/student_model.db "$VM:$DEST/storage/sqlite/"
rsync -avz storage/curriculum/units.json "$VM:$DEST/storage/curriculum/"
rsync -avz data/curated_keep.json "$VM:$DEST/data/"
echo "migration copy done"

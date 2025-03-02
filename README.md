# ♟️ Chess Game in Pygame  
A Python-based chess game using Pygame, with fully interactive piece movement, rule enforcement, and special moves.  

---

## 🚀 TODO Roadmap  

This project follows this roadmap to ensure a smooth development process. Follow along as the chess game evolves!  

---

### 🎨 **1️⃣ Set Up the Chessboard Display**  
- [ ] 🖥 **Initialize Pygame** in `main.py`  
- [ ] 🎨 **Create game constants** (`WIDTH`, `HEIGHT`, etc.)  
- [ ] 🏁 **Set up board colors** (`LIGHT`, `DARK`)  
- [ ] 📏 **Write `draw_board()` function**  
- [ ] 🪟 **Create the game window**  

---

### 🏇 **2️⃣ Load & Display Pieces**

---

### 🔧 **3️⃣ Create a `Piece` Base Class**  
- [ ] 📜 **Define `Piece` class** in `piece.py`

---

### ⚔️ **4️⃣ Implement Movement for Each Piece**  

#### 👑 **Major Pieces First**  
- [ ] 🏇 **`Knight` (`knight.py`)** → Moves in L-shapes 
- [ ] 🏗 **`Rook` (`rook.py`)** → Moves in straight lines  
- [ ] 🎭 **`Bishop` (`bishop.py`)** → Moves diagonally  
- [ ] 👸 **`Queen` (`queen.py`)** → Combines rook & bishop moves   
- [ ] 🤴 **`King` (`king.py`)** → Moves one square in any direction  

#### 🏰 **Then Pawns**  
- [ ] 🚶 **Implement `Pawn` class (`pawn.py`)**  
- [ ] 📜 **Define `valid_moves()` for pawns**  
- [ ] ✅ **Test pawn movement before proceeding**  

---

### 🖱 **5️⃣ Handle Player Interaction**  
- [ ] 🖲 **Handle mouse events for selection & movement**

---

### 📜 **6️⃣ Validate Moves & Enforce Rules**  
- [ ] ✅ **Allow only legal moves**  
- [ ] 🚫 **Prevent jumping (except knights)**  
- [ ] 🔄 **Enforce turn-based play (White first, then Black)**  

---

### 🎯 **7️⃣ Special Rules & Features**  
- [ ] 🔄 **Castling (king & rook)**  
- [ ] ♟️ **Pawn promotion**  
- [ ] 🏹 **En passant**  

---

### 🎨 **8️⃣ Final Enhancements**  
- [ ] 🔄 **Code refactoring**   
- [ ] ♜ **Display captured pieces**  
- [ ] 🔄 **Add a restart button**  

---

## 🔧 How to Run the Game  
```bash
git clone https://github.com/trev-the-dev/chess.git
cd chess
python main.py